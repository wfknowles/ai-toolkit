{
  "schema_version": "1.1",
  "description": "Structured object capturing essential state and context between collaborative sessions.",
  "type": "object",
  "properties": {
    "session_metadata": {
      "type": "object",
      "properties": {
        "end_timestamp": {"type": "string", "format": "date-time", "description": "Timestamp when the session synthesis concluded."},
        "state_object_version": {"type": "string", "description": "Version of this state object instance."},
        "generating_schema_version": {"type": "string", "const": "1.1", "description": "Version of the schema used to generate this object."}
      },
      "required": ["end_timestamp", "state_object_version", "generating_schema_version"]
    },
    "project_context": {
      "type": "object",
      "properties": {
        "overall_analytical_goal": {"type": "string", "description": "User's high-level objective for the overarching analysis."},
        "meta_goal": {"type": "string", "description": "User's objective regarding refinement of process/personas."},
        "source_document_reference": {"type": "string", "description": "Identifier for the primary document being analyzed (e.g., 'serverless.yml vCurrent')."}
      },
      "required": ["overall_analytical_goal"]
    },
    "methodology_context": {
      "type": "object",
      "properties": {
        "primary_ai_persona_for_next_session": {"type": "string", "description": "The persona_id the AI should adopt at the start of the next session."},
        "agreed_interaction_style": {"type": "string", "description": "Summary of the established interaction method (e.g., 'Persona-driven contracts')."},
        "available_expert_personas_list": {"type": "array", "items": {"type": "string"}, "description": "List of persona_ids available."},
        "key_epistemological_commitments_ref": {"type": "string", "description": "Reference to the agreed-upon philosophical/ethical stance (e.g., 'Per Dr. Aris Thorne V2 definition')."}
      },
      "required": ["primary_ai_persona_for_next_session"]
    },
    "artifact_manifest": {
      "type": "array",
      "description": "List of key artifacts (personas, schemas, checklists, prompts) created or modified.",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string", "description": "Human-readable name of the artifact."},
          "version": {"type": "string", "description": "Version identifier for the artifact."},
          "status": {"type": "string", "enum": ["Defined", "Benchmarked", "Generated", "Partially Generated", "Revised", "Deprecated"], "description": "Current status."},
          "id_or_reference": {"type": "string", "optional": true, "description": "Schema ID or unique reference if applicable."},
          "details": {"type": "string", "optional": true, "description": "Brief notes on status or contents."}
        },
        "required": ["name", "version", "status"]
      }
    },
    "session_summary_state": {
      "type": "object",
      "properties": {
        "last_completed_phase_action": {"type": "string", "description": "Description of the last significant step finished."},
        "key_learnings_insights": {"type": "array", "items": {"type": "string"}, "description": "Bulleted list of key takeaways from the session."},
        "current_state_of_data_analysis": {"type": "string", "description": "Summary of progress on the primary analysis task."},
        "open_questions_or_issues": {"type": "array", "items": {"type": "string"}, "description": "List of unresolved items."}
      },
      "required": ["last_completed_phase_action"]
    },
    "next_session_focus": {
      "type": "object",
      "properties": {
        "immediate_next_step": {"type": "string", "description": "The specific, actionable task to start the next session."},
        "intended_persona_for_next_step": {"type": "string", "description": "The suggested persona_id to handle the next step."}
      },
      "required": ["immediate_next_step"]
    }
  },
  "required": ["session_metadata", "project_context", "methodology_context", "artifact_manifest", "session_summary_state", "next_session_focus"]
}