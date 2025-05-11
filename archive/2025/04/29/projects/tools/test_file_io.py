import unittest
import os
import shutil
import tempfile
from .file_io import read_file_tool, _is_path_allowed

class TestFileIO(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory structure mirroring expected allow lists
        self.test_dir = tempfile.mkdtemp()
        self.project_root = self.test_dir # Simulate project root for tests
        self.data_dir = os.path.join(self.test_dir, 'data')
        self.docs_dir = os.path.join(self.test_dir, 'docs')
        self.editable_dir = os.path.join(self.data_dir, 'editable')
        self.other_dir = os.path.join(self.test_dir, 'other')

        os.makedirs(self.data_dir)
        os.makedirs(self.docs_dir)
        os.makedirs(self.editable_dir)
        os.makedirs(self.other_dir)

        # Create dummy files
        self.allowed_read_file = os.path.join(self.data_dir, 'readable.txt')
        self.allowed_edit_file = os.path.join(self.editable_dir, 'editable.txt')
        self.disallowed_file = os.path.join(self.other_dir, 'secret.txt')
        self.nonexistent_file = os.path.join(self.data_dir, 'nonexistent.txt')

        with open(self.allowed_read_file, 'w') as f:
            f.write("Readable content.")
        with open(self.allowed_edit_file, 'w') as f:
            f.write("Editable content.")
        with open(self.disallowed_file, 'w') as f:
            f.write("Secret content.")

        # --- Monkey patch the configuration for testing ---
        # Ideally, use dependency injection, but for simplicity here, we patch
        import src.tools.file_io
        self.original_read_allow_list = src.tools.file_io.READ_ALLOW_LIST
        self.original_edit_allow_list = src.tools.file_io.EDIT_ALLOW_LIST
        src.tools.file_io.READ_ALLOW_LIST = [self.data_dir, self.docs_dir]
        src.tools.file_io.EDIT_ALLOW_LIST = [self.editable_dir]
        # Patch project root used in _is_path_allowed if it relies on module path
        self.original_project_root = src.tools.file_io.PROJECT_ROOT
        src.tools.file_io.PROJECT_ROOT = self.project_root

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)
        # Restore original config
        import src.tools.file_io
        src.tools.file_io.READ_ALLOW_LIST = self.original_read_allow_list
        src.tools.file_io.EDIT_ALLOW_LIST = self.original_edit_allow_list
        src.tools.file_io.PROJECT_ROOT = self.original_project_root

    # --- Test _is_path_allowed --- (Helper function test)
    def test_is_path_allowed_valid(self):
        is_allowed, path = _is_path_allowed(self.allowed_read_file, [self.data_dir])
        self.assertTrue(is_allowed)
        self.assertEqual(path, os.path.normpath(self.allowed_read_file))

    def test_is_path_allowed_valid_subdirectory(self):
        is_allowed, path = _is_path_allowed(self.allowed_edit_file, [self.data_dir]) # data_dir should allow subdirs
        self.assertTrue(is_allowed)
        self.assertEqual(path, os.path.normpath(self.allowed_edit_file))

    def test_is_path_allowed_invalid(self):
        is_allowed, path = _is_path_allowed(self.disallowed_file, [self.data_dir, self.docs_dir])
        self.assertFalse(is_allowed)
        self.assertEqual(path, "")

    def test_is_path_allowed_traversal_attempt_simple(self):
        traversal_path = os.path.join(self.data_dir, '..', 'other', 'secret.txt')
        is_allowed, path = _is_path_allowed(traversal_path, [self.data_dir])
        self.assertFalse(is_allowed) # Should resolve to disallowed_file and fail

    def test_is_path_allowed_traversal_root_relative(self):
        # Construct a path that tries to go above the *intended* allowed root using ..
        # even if it resolves to somewhere technically allowed by a different rule
        traversal_path = os.path.join(self.editable_dir, '..', '..', 'docs', 'doc.txt') # Tries to escape data/editable
        # Test against EDIT_ALLOW_LIST which only has editable_dir
        is_allowed, path = _is_path_allowed(traversal_path, [self.editable_dir])
        self.assertFalse(is_allowed)

    def test_is_path_allowed_nonexistent(self):
        # Should still validate path structure even if file doesn't exist yet
        is_allowed, path = _is_path_allowed(self.nonexistent_file, [self.data_dir])
        self.assertTrue(is_allowed)
        self.assertEqual(path, os.path.normpath(self.nonexistent_file))

    # --- Test read_file_tool ---
    def test_read_file_tool_success(self):
        result = read_file_tool(self.allowed_read_file)
        self.assertTrue(result['success'])
        self.assertEqual(result['content'], "Readable content.")
        self.assertIsNone(result['error'])

    def test_read_file_tool_access_denied(self):
        result = read_file_tool(self.disallowed_file)
        self.assertFalse(result['success'])
        self.assertIsNone(result['content'])
        self.assertEqual(result['error'], "Access Denied: Path is not allowed.")

    def test_read_file_tool_not_found(self):
        result = read_file_tool(self.nonexistent_file)
        self.assertFalse(result['success'])
        self.assertIsNone(result['content'])
        self.assertEqual(result['error'], "File Not Found.")

    def test_read_file_tool_path_is_directory(self):
        result = read_file_tool(self.data_dir)
        self.assertFalse(result['success'])
        self.assertIsNone(result['content'])
        self.assertEqual(result['error'], "Invalid Path: Not a file.")

    def test_read_file_tool_traversal_denied(self):
        traversal_path = os.path.join(self.data_dir, '..', 'other', 'secret.txt')
        result = read_file_tool(traversal_path)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Access Denied: Path is not allowed.")

    # --- Tests for edit_file_tool ---
    def test_edit_file_tool_success(self):
        new_content = "Approved new content."
        result = file_io.edit_file_tool(self.allowed_edit_file, new_content)
        self.assertTrue(result['success'], f"Edit failed unexpectedly: {result.get('error')}")
        self.assertIsNone(result['error'])
        # Verify content was written
        with open(self.allowed_edit_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, new_content)

    def test_edit_file_tool_success_create_new(self):
        new_file_path = os.path.join(self.editable_dir, 'newly_editable.txt')
        new_content = "Content for a new file."
        # Ensure file doesn't exist initially
        self.assertFalse(os.path.exists(new_file_path))

        result = file_io.edit_file_tool(new_file_path, new_content)
        self.assertTrue(result['success'], f"Edit failed unexpectedly: {result.get('error')}")
        self.assertIsNone(result['error'])
        # Verify file was created and content written
        self.assertTrue(os.path.exists(new_file_path))
        with open(new_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, new_content)

    def test_edit_file_tool_access_denied_read_path(self):
        # Trying to edit a file that is only in the read allow list
        new_content = "Attempt to edit read-only allowed file."
        result = file_io.edit_file_tool(self.allowed_read_file, new_content)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Access Denied: Path is not allowed for editing.")
        # Verify original content unchanged
        with open(self.allowed_read_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Readable content.")

    def test_edit_file_tool_access_denied_other_path(self):
        # Trying to edit a file in a completely disallowed directory
        new_content = "Attempt to edit disallowed file."
        result = file_io.edit_file_tool(self.disallowed_file, new_content)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Access Denied: Path is not allowed for editing.")

    def test_edit_file_tool_path_is_directory(self):
        new_content = "Attempt to overwrite directory."
        result = file_io.edit_file_tool(self.editable_dir, new_content)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Invalid Path: Cannot edit, not a file.")

    def test_edit_file_tool_traversal_denied(self):
        traversal_path = os.path.join(self.editable_dir, '..', 'other_secret.txt') # Try to escape editable dir
        new_content = "Traversal edit attempt."
        result = file_io.edit_file_tool(traversal_path, new_content)
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Access Denied: Path is not allowed for editing.")

if __name__ == '__main__':
    # Add file_io module import for running directly
    import sys
    # Ensure src directory is in path if running test file directly
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from src.tools import file_io
    unittest.main() 