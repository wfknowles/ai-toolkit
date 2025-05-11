# Project Roadmap: File-Based AI Brain V1

This document outlines the development roadmap for implementing the file-based AI agent brain, based on the requirements defined in `requirements.md` and subsequent planning discussions (2024-04-25 Simulated).

## 1. Project Phases and Milestones

The project is divided into two main phases, with Phase 1 further broken down into milestones:

*   **Phase 1: Core Metadata Indexing & Retrieval (R1)**
    *   **Milestone 1a:** YAML Frontmatter Parsing & Validation Logic
    *   **Milestone 1b:** Indexer Script Core & JSON Index Generation
    *   **Milestone 1c:** Retrieval Module - Metadata Query Methods
    *   **Milestone 1d:** Basic Integration, Testing & Dependency Setup
*   **Phase 2: Semantic Search Enhancement (R2) (Optional - Post-R1)**
    *   **Milestone 2a:** Embedding Generation Integration (Indexer)
    *   **Milestone 2b:** Faiss Index Construction (Indexer)
    *   **Milestone 2c:** Semantic Search Method (Retrieval Module)
    *   **Milestone 2d:** Semantic Search Integration & Testing

## 2. Phase 1 User Stories and Tasks

### Milestone 1a: YAML Frontmatter Parsing & Validation Logic

*   **User Story 1 (US1): Knowledge File Metadata Enforcement**
    *   *As a Developer, I want a standard YAML frontmatter schema enforced so that knowledge files have consistent metadata for indexing.*
    *   **Notes:** Schema defined in `requirements.md` (Sec 1.1). Mandatory: `title`, `keywords`, `topics`. Use `PyYAML`. Target dir: `knowledge/`.
    *   **Tasks:**
        *   **Task 1.1:** Implement YAML parsing function `parse_frontmatter(file_path)` using `PyYAML.safe_load`.
            *   *Code Hint:* Handle potential `yaml.YAMLError`.
            ```python
            import yaml
            from pathlib import Path
            import logging

            def parse_frontmatter(file_path: Path) -> dict | None:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Simple frontmatter split (improve with regex if needed)
                        if content.startswith('---\n'):
                            parts = content.split('---\n', 2)
                            if len(parts) >= 3:
                                frontmatter = yaml.safe_load(parts[1])
                                # TODO: Add validation logic here (Task 1.2)
                                return frontmatter
                except FileNotFoundError:
                    logging.error(f"File not found: {file_path}")
                except yaml.YAMLError as e:
                    logging.error(f"YAML parsing error in {file_path}: {e}")
                except Exception as e: # Catch other potential errors
                     logging.error(f"Error processing file {file_path}: {e}")
                return None
            ```
        *   **Task 1.2:** Implement validation logic within `parse_frontmatter` to check for mandatory fields (`title`, `keywords`, `topics`) and basic types (e.g., keywords/topics are lists).
            *   *Code Hint:* Add checks after `yaml.safe_load`.
        *   **Task 1.3:** Add robust error handling and logging (using Python `logging` module) for parsing/validation errors (log message should include filename).
        *   **Task 1.4:** Write unit tests (`pytest`, `pyfakefs`) for `parse_frontmatter` covering valid files, files with missing mandatory fields, files with invalid YAML, and non-existent files.

### Milestone 1b: Indexer Script Core & JSON Index Generation

*   **User Story 2 (US2): Metadata Index Generation**
    *   *As an AI Agent System, I need a script that generates a JSON index from knowledge file metadata so that information can be retrieved quickly.*
    *   **Notes:** Script `indexer.py`. CLI: `python indexer.py --source-dir <path> --index-dir <path> [--log-level <level>]`. Output: `brain/index/master_index.json` (schema 1.2 in `requirements.md`). Uses US1 parsing logic. Requires atomic write. Use `argparse`, `logging`, `pathlib`, `json`, `tempfile`, `os`.
    *   **Tasks:**
        *   **Task 2.1:** Set up `indexer.py` CLI using `argparse` for `--source-dir`, `--index-dir`, `--log-level`.
        *   **Task 2.2:** Implement file scanning logic using `pathlib.Path(source_dir).rglob('*.md')`.
        *   **Task 2.3:** Integrate `parse_frontmatter` function (US1) for each discovered Markdown file.
        *   **Task 2.4:** Implement logic to populate the `metadata`, `keyword_index`, and `topic_index` dictionaries based on parsed frontmatter. Ensure keywords/topics in indices are lowercased. Store file paths relative to the `brain` directory if possible, or relative to `--source-dir` consistently.
        *   **Task 2.5:** Implement atomic write for `master_index.json` using `tempfile.NamedTemporaryFile` and `os.rename` (or `shutil.move`).
            *   *Diagram/Logic:* `Write to temp file -> Close temp file -> Rename temp file to target file`
        *   **Task 2.6:** Configure standard Python `logging` based on `--log-level`. Log start/end, number of files processed, errors encountered, and successful index write.
        *   **Task 2.7:** Add unit tests for the main indexing logic (mocking file system) and the atomic write process.

### Milestone 1c: Retrieval Module - Metadata Query Methods

*   **User Story 3 (US3): Metadata Retrieval API**
    *   *As an AI Agent Developer, I want a Python module that provides simple methods to query the generated metadata index so that I can easily retrieve relevant knowledge file information.*
    *   **Notes:** Module `retrieval_module.py`, Class `RetrievalModule`. Load `master_index.json` on `__init__`. Methods: `search_metadata`, `lookup_by_keyword`, `lookup_by_topic` (specs 1.4 in `requirements.md`). Handle `FileNotFoundError`. Case-insensitive.
    *   **Tasks:**
        *   **Task 3.1:** Implement `RetrievalModule` class structure in `retrieval_module.py`.
        *   **Task 3.2:** Implement `__init__(self, index_dir: str)`: constructs path to `master_index.json`, loads it using `json.load`, stores data in instance variables. Include try-except for `FileNotFoundError` and `json.JSONDecodeError`.
            *   *Code Hint:* Store the loaded dict (e.g., `self._index_data`).
        *   **Task 3.3:** Implement `lookup_by_keyword(self, keyword: str) -> list[str]`: Lookup lowercase keyword in `self._index_data['keyword_index']`. Return empty list if not found.
        *   **Task 3.4:** Implement `lookup_by_topic(self, topic: str) -> list[str]`: Lookup lowercase topic in `self._index_data['topic_index']`. Return empty list if not found.
        *   **Task 3.5:** Implement `search_metadata(self, query: str, search_fields: list = ...) -> list[dict]`: Iterate through `self._index_data['metadata']`. For each file's metadata, check if lowercase `query` string exists in any of the lowercase string/list values of the specified `search_fields`. Return list of full metadata dicts for matching files.
            *   *Optimization Note:* This is a basic linear scan. If performance becomes an issue with many files, consider pre-indexing text fields or using a more optimized search structure later.
        *   **Task 3.6:** Add detailed docstrings and type hints to the class and methods.
        *   **Task 3.7:** Write unit tests for all retrieval methods, including initialization errors, successful lookups, lookups for non-existent keys, and metadata search results.

### Milestone 1d: Basic Integration, Testing & Dependency Setup

*   **User Story 4 (US4): Basic Integration & Dependency Management**
    *   *As a Developer, I need the core components (indexer, retriever) to work together with pinned dependencies so that the basic system is stable and testable.*
    *   **Notes:** Create `requirements.txt`. Develop simple end-to-end test. Add basic READMEs.
    *   **Tasks:**
        *   **Task 4.1:** Create `requirements.txt` listing `PyYAML==<version>`. Add `pytest==<version>` and `pyfakefs==<version>` under a `dev-requirements.txt` or similar.
            *   *Action:* Run `pip freeze > requirements.txt` after installing `PyYAML` to get version.
        *   **Task 4.2:** Create an integration test script (e.g., `tests/test_integration.py`): Uses `pyfakefs` to set up mock files with frontmatter, runs `indexer.py` (using `subprocess` or by importing its main function), initializes `RetrievalModule`, performs lookups (`lookup_by_keyword`, `search_metadata`), asserts expected results.
        *   **Task 4.3:** Create `README.md` for `indexer.py` explaining CLI usage.
        *   **Task 4.4:** Create `README.md` for `retrieval_module.py` explaining class usage and methods.

## 3. Phase 2 User Stories and Tasks (High-Level)

*(Details to be refined if/when Phase 2 is initiated)*

*   **User Story 5 (US5): Semantic Index Generation**
    *   *As an AI Agent System, I need the indexer script to optionally generate text embeddings and a Faiss index so that semantic similarity search is possible.*
    *   **Tasks:** Add `--embeddings` flag logic, implement chunking, integrate `sentence-transformers`, generate embeddings, build Faiss index (`IndexFlatL2`), save index and map file (`embedding_map.json`), update `master_index.json` with paths.
*   **User Story 6 (US6): Semantic Retrieval API**
    *   *As an AI Agent Developer, I want the Retrieval Module to provide a method to find knowledge chunks semantically similar to a query text.*
    *   **Tasks:** Implement `find_similar` method, load Faiss index and map file, embed query text, perform Faiss search, map results back to file paths/chunk IDs.
*   **User Story 7 (US7): Semantic Search Dependencies & Integration**
    *   *As a Developer, I need semantic search dependencies managed and the feature integrated and tested end-to-end.*
    *   **Tasks:** Add `sentence-transformers==<version>`, `faiss-cpu==<version>` (or `faiss-gpu`) to `requirements.txt`. Update integration tests to cover `find_similar`. Update READMEs.

## 4. Key Considerations & Future Work

*   **Indexer Triggering:** Initial plan is manual execution. Recommended deployment involves scheduling (e.g., cron job).
*   **Concurrency:** Current design assumes single indexer process and single agent reader (or infrequent index updates). Concurrent read/write requires significant changes (locking mechanisms).
*   **Knowledge Contribution UX:** Requires clear documentation and potentially a validation tool (`indexer.py --validate-only`?).
*   **Scalability:** Monitor Faiss index size/performance and `search_metadata` performance. Consider Faiss index upgrades (IVF, HNSW) or optimizing metadata search if needed.
*   **Error Handling & Logging:** Continuously refine based on testing and usage.
*   **Configuration:** Consider externalizing settings like embedding model name (G7 from `requirements.md`).
*   **Context Handling:** Logic for processing retrieved context (summarization, snippeting) needs to be built separately, likely interacting with the Retrieval Module's output. 