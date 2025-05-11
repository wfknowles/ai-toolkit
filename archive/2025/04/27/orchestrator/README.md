# MotM Orchestrator Refactor: README

## Overview
This orchestrator implements the Meeting of the Minds (MotM) workflow for collaborative requirements and roadmap generation. The refactored version introduces a user-friendly interface, dynamic inputs, and improved output management.

## Key Features
- Accepts `output_dir` and `concept` as user inputs via a main interface prompt
- Removes hardcoded values from the orchestrator logic
- Passes dynamic values through state and step prompts
- Adds verification and cleanup steps to ensure only final outputs remain
- Follows strict interface contracts and naming conventions

## Workflow Steps
1. User runs the main interface prompt and provides:
   - `output_dir`: Directory for final outputs
   - `concept`: Project or idea to analyze
2. Orchestrator executes all MotM steps, passing inputs through state
3. After generating requirements and roadmap, the workflow:
   - Verifies both files exist and are non-empty
   - Cleans up all auxiliary files
4. Only the final outputs remain in the specified directory

## How to Use
1. Fill out the main interface prompt in the MotM prompt directory
2. Run the orchestrator
3. Review the outputs in your chosen directory

## Step Order
- All original MotM steps
- `step-14-verify-outputs.prompt`
- `step-15-cleanup.prompt`
- Completion

## Interface Contract
- All step prompts must return JSON per INTERFACE_CONTRACT.md
- State is managed per state.schema.json

## Maintenance
- To add new steps, update STEP_ORDER and follow the interface contract
- For troubleshooting, check state.json and orchestrator logs 