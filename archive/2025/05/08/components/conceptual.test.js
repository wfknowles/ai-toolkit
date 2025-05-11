// tests/by_task/code_generation/python/function_from_spec.test.js
// Illustrative Jest test for a Python code generation prompt

const fs = require('fs');
const path = require('path');
// Assume an LLM interaction module (mockable for unit tests)
const { executePromptAgainstLlm } = require('../../../llm_service_mock'); // Adjust path
// Assume a helper to load prompt files (e.g., parsing metadata and body)
const { loadPromptFromFile } = require('../../../prompt_loader'); // Adjust path

describe('Python Function from Specification Prompt', () => {
  const promptPath = path.join(__dirname, '../../../../prompts/by_task/code_generation/python/function_from_spec.md');
  const exemplarBasePath = path.join(__dirname, '../../../../exemplars/by_task/code_generation/python/');

  let promptDefinition;

  beforeAll(() => {
    // Load the prompt definition (metadata and body)
    promptDefinition = loadPromptFromFile(promptPath);
  });

  test('should generate a valid Python function for basic addition', async () => {
    const inputSpec = fs.readFileSync(path.join(exemplarBasePath, 'add_numbers_input.txt'), 'utf-8');
    const expectedOutputCode = fs.readFileSync(path.join(exemplarBasePath, 'add_numbers_expected_output.py'), 'utf-8');

    // Assume promptDefinition.body is the template string
    // and we have a templating engine or simple replace for parameters
    const populatedPromptBody = promptDefinition.body
      .replace('{{ specification }}', inputSpec)
      .replace('{{ function_name_suggestion }}', 'add_two_numbers');

    const llmResponse = await executePromptAgainstLlm({
      prompt: populatedPromptBody,
      // llmModel: promptDefinition.metadata.llm_compatibility[0], // Use compatible model
      // temperature: 0.2, // Set deterministic temperature for testing
    });

    // Basic check: Does the output contain 'def add_two_numbers'?
    expect(llmResponse.output).toContain('def add_two_numbers');
    // Basic check: Does it seem like Python code? (very simplistic)
    expect(llmResponse.output).toMatch(/def\s+\w+\(.*\):/);

    // More advanced:
    // 1. Validate Python syntax of llmResponse.output (e.g., using a Python parser or linter)
    // validatePythonSyntax(llmResponse.output); // Fictitious function

    // 2. Compare AST or functional equivalence if possible (complex)

    // 3. For simplicity here, let's assume a direct (or cleaned) comparison for this example
    // In reality, output might have slight variations.
    // Cleaning whitespace for a more robust comparison:
    const cleanLlmOutput = llmResponse.output.replace(/\s+/g, ' ').trim();
    const cleanExpectedOutput = expectedOutputCode.replace(/\s+/g, ' ').trim();
    expect(cleanLlmOutput).toEqual(cleanExpectedOutput);
  });

  test('should include type hints as per requirements', async () => {
    const inputSpec = fs.readFileSync(path.join(exemplarBasePath, 'greet_user_input.txt'), 'utf-8');
    const populatedPromptBody = promptDefinition.body
      .replace('{{ specification }}', inputSpec)
      .replace('{{ function_name_suggestion }}', 'greet');
    
    const llmResponse = await executePromptAgainstLlm({ prompt: populatedPromptBody });

    expect(llmResponse.output).toMatch(/name: str/) // Check for type hint on parameter
    expect(llmResponse.output).toMatch(/-> str:/)   // Check for return type hint
  });

  // Add more test cases for:
  // - Error handling generation
  // - PEP 8 compliance (could run a linter on the output)
  // - Handling of complex specifications
  // - Edge cases for inputs
});