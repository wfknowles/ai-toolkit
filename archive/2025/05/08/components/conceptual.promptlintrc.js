// .promptlintrc.js
// Conceptual configuration for a custom prompt linter

module.exports = {
    // Define extends if we are using a base linter and adding to it
    // extends: 'some-base-linter-config',
  
    // Define global settings for the linter
    settings: {
      targetLlmModels: ['GPT-4', 'Claude-3-Opus'], // For compatibility checks
      maxContextLengthChars: 15000, // Example character limit for context
      maxPromptLengthChars: 4000, // Example character limit for the prompt body itself
    },
  
    // Custom parsers or plugins if prompts are in a specific format (e.g., structured MD)
    // plugins: [
    //   'prompt-metadata-parser',
    //   'prompt-security-checker',
    // ],
  
    // Define specific rules and their severity (off: 0, warn: 1, error: 2)
    rules: {
      // Rules based on Prompt Engineering Standard #1: Explicit Intent & Task Definition
      'require-llm-persona': ['error', { message: 'Prompt must specify an LLM persona (e.g., "Act as a...").' }],
      'require-task-definition': ['error', { message: 'Prompt must include a clear task definition.' }],
      'require-output-format': ['warn', { message: 'Prompt should specify the desired output format.' }],
      'no-vague-phrases': ['warn', { prohibited: ['some code', 'a thing', 'etc.'], suggestion: 'Be more specific.' }],
  
      // Rules based on Standard #2: Context
      'check-context-placeholder-format': ['error', { format: /\{\{\s*[\w-]+\s*\}\}/ }], // Enforce {{variable}}
      // 'warn-large-context': ['warn', { maxLength: 'settings.maxContextLengthChars' }], // Use setting
      'detect-pii-in-prompt-context': ['error', { patternsFile: './lint_rules/pii_patterns.txt' }], // External file for regex/keywords
      'detect-secrets-in-prompt-context': ['error', { patternsFile: './lint_rules/secrets_patterns.txt' }],
  
      // Rules based on Standard #4: Parameterization
      'enforce-parameter-documentation': ['error', { message: 'Templated prompts must document parameters in metadata.' }],
  
      // Rules based on Standard #5: Security (Prompt Injection)
      'require-input-demarcation': ['warn', { message: 'User input within prompts should be clearly demarcated (e.g., using <user_input> tags).' }],
  
      // Rules based on Standard #7 & #8: Documentation & Templates
      'require-prompt-metadata': ['error', { fields: ['prompt_id', 'title', 'version', 'status', 'author'] }],
      'encourage-few-shot-example-section': ['info', { message: 'Consider adding a "## Few-Shot Examples" section for complex tasks.' }],
  
      // Rules based on Standard #9: Ethical/Bias
      'detect-harmful-content-generation-requests': ['error', { patternsFile: './lint_rules/harmful_request_patterns.txt' }],
      'encourage-bias-mitigation-statements': ['info', { message: 'For prompts generating diverse content, consider adding bias mitigation instructions.' }],
  
      // General Rules
      // 'check-prompt-body-length': ['warn', { maxLength: 'settings.maxPromptLengthChars' }],
      'no-excessive-capitalization': 'warn',
      'check-grammar-spelling': ['info', { language: 'en-US' }], // Placeholder for potential integration
    },
  };