# TypeScript Type Generation

This document explains the automatic TypeScript type generation process from Pydantic models in the OpenAgents JSON project.

## Overview

The OpenAgents JSON project uses Pydantic models for data validation and serialization in the backend. To ensure type safety and consistency between the backend and frontend, we automatically generate TypeScript type definitions from these Pydantic models.

## How It Works

1. We use the [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) library to convert Pydantic models to TypeScript interfaces.
2. A script (`scripts/generate_types.py`) automatically runs this conversion for key model files.
3. The generated TypeScript files are stored in `openagents_json/ui/src/types/generated/`.
4. A Git pre-commit hook ensures that the TypeScript types are always up to date.
5. A CI workflow checks that the TypeScript types match what would be generated from the current Pydantic models.

## Setup

To set up the type generation tools:

1. Install the required dependencies:
   ```bash
   pip install datamodel-code-generator
   ```

2. Set up the Git pre-commit hook:
   ```bash
   python scripts/setup_git_hooks.py
   ```

## Manual Generation

You can manually generate the TypeScript types by running:

```bash
python scripts/generate_types.py
```

This will:
1. Read the Pydantic models from:
   - `openagents_json/workflow/models.py`
   - `openagents_json/workflow/validator/base.py`
2. Generate TypeScript interfaces and save them to:
   - `openagents_json/ui/src/types/generated/workflow.ts`
   - `openagents_json/ui/src/types/generated/validation.ts`

## Using the Generated Types

In your TypeScript/React code, you can import and use the generated types:

```typescript
import { Workflow, WorkflowStep, Connection } from '../types/generated/workflow';
import { ValidationResult, ValidationError } from '../types/generated/validation';

// Use the types in your code
const workflow: Workflow = {
  // ...
};
```

## Best Practices

1. **Never modify the generated files directly** - They will be overwritten when the generation script runs.
2. **Keep Pydantic models as the single source of truth** - All changes to data structures should start in the Pydantic models.
3. **Run the generation script after changing Pydantic models** - This ensures the frontend types stay in sync.
4. **Add the generated files to your commits** - This allows other developers to use the latest types without running the generation script.

## Troubleshooting

### Types are not up to date

If you get an error about types not being up to date:

1. Make sure you have the latest Pydantic models.
2. Run the generation script: `python scripts/generate_types.py`
3. Add the changes to your commit: `git add openagents_json/ui/src/types/generated/`

### Generation fails

If the type generation fails:

1. Check that datamodel-code-generator is installed: `pip install datamodel-code-generator`
2. Check that the input Pydantic model files exist and are valid Python files.
3. Check the error message for specific issues with the models.

## CI Integration

We have a GitHub workflow that checks if the generated types match the current Pydantic models. If they don't match, the workflow will fail.

This ensures that all changes to Pydantic models are accompanied by the corresponding TypeScript type updates. 