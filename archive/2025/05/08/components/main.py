# app/main.py (Conceptual FastAPI Application)

from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field
import os
import logging
from typing import Dict, Any, List, Optional

# Assume helper modules exist for loading/parsing/templating prompts
from .prompt_loader import load_prompt_template, PromptNotFoundException, TemplateParameterMissingException
from .templating import populate_template
from .audit_logger import log_interaction # For Standard #10 & Component #14

# Configure logging (can be more sophisticated)
log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

# --- Pydantic Models for API Request/Response ---
class PromptRequest(BaseModel):
    prompt_id: str = Field(..., description="Unique ID of the prompt or template to use.")
    context: Dict[str, Any] = Field({}, description="Key-value pairs for populating template parameters.")
    requestor_info: Optional[Dict[str, str]] = Field(None, description="Info about the requestor for audit logs.")

class PromptResponse(BaseModel):
    prompt_id_requested: str
    prompt_version_used: str # Fetched from prompt metadata
    constructed_prompt: str
    warnings: List[str] = []

# --- FastAPI Application Instance ---
app = FastAPI(
    title="Prompt Backend Service",
    description="Serves dynamically constructed prompts based on templates and context.",
    version="1.0.0",
)

# --- API Endpoints ---
@app.post("/api/v1/get_prompt", response_model=PromptResponse, status_code=status.HTTP_200_OK)
async def get_constructed_prompt(request: PromptRequest, http_request: Request):
    """
    Retrieves a prompt template, populates it with provided context,
    and returns the fully constructed prompt.
    """
    logger.info(f"Received request for prompt_id: {request.prompt_id}")
    warnings = []

    try:
        # 1. Load the prompt template definition (metadata and body)
        # This function would read from the PROMPT_LIB_PATH env var
        prompt_metadata, prompt_template_body = load_prompt_template(request.prompt_id)
        prompt_version = prompt_metadata.get("version", "unknown")
        logger.debug(f"Loaded template version: {prompt_version}")

        # 2. Validate provided context against required parameters in metadata (if applicable)
        # (Simplified - real validation would be more robust)
        required_params = [p.get('name') for p in prompt_metadata.get('parameters', []) if p.get('required')]
        missing_params = [p for p in required_params if p not in request.context]
        if missing_params:
            raise TemplateParameterMissingException(f"Missing required context parameters: {', '.join(missing_params)}")

        # 3. Populate the template
        constructed_prompt = populate_template(prompt_template_body, request.context)
        logger.debug("Template populated successfully.")

        # 4. (Optional) Add any standard prefixes/suffixes or safety instructions
        # constructed_prompt = add_safety_wrappers(constructed_prompt)

        # 5. Log the interaction for auditing (Component #14)
        # Be mindful of logging sensitive context if necessary
        log_interaction(
            requestor=request.requestor_info,
            prompt_id=request.prompt_id,
            prompt_version=prompt_version,
            context_keys=list(request.context.keys()), # Log keys only, not values, for privacy?
            # full_prompt_hash=hash_prompt(constructed_prompt) # Log hash instead of full prompt?
            outcome="success",
        )

        return PromptResponse(
            prompt_id_requested=request.prompt_id,
            prompt_version_used=prompt_version,
            constructed_prompt=constructed_prompt,
            warnings=warnings, # Add any non-critical warnings here
        )

    except PromptNotFoundException:
        logger.error(f"Prompt template not found: {request.prompt_id}")
        log_interaction(requestor=request.requestor_info, prompt_id=request.prompt_id, outcome="error - not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prompt '{request.prompt_id}' not found.")
    except TemplateParameterMissingException as e:
        logger.error(f"Error populating template {request.prompt_id}: {e}")
        log_interaction(requestor=request.requestor_info, prompt_id=request.prompt_id, outcome="error - missing params")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error processing request for prompt_id: {request.prompt_id}")
        log_interaction(requestor=request.requestor_info, prompt_id=request.prompt_id, outcome="error - internal server error")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error processing prompt request.")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok"}

# --- Helper Modules (Conceptual - would be in separate files) ---
# module: app/prompt_loader.py
# contains load_prompt_template(prompt_id) -> (metadata_dict, body_str)
# module: app/templating.py
# contains populate_template(template_str, context_dict) -> populated_str
# module: app/audit_logger.py
# contains log_interaction(...)