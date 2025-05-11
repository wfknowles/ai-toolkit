# AI Agent Engineer - Round 3 Interview (Orchestrator Framework)

**Facilitator:** If confirmation is transparent, how does the agent provide useful status while waiting, avoiding misleading the user?

**AI Agent Engineer:** (Placeholder suggesting the Orchestrator might need to send an intermediate "WaitingForConfirmation" status back to the agent, which the agent translates to "Waiting for user confirmation..." rather than implying execution has started.)

**Facilitator:** Detail the agent logic for parsing `USER_REJECTED_EDIT` vs `EXECUTION_FAILED_POST_CONFIRMATION`.

**AI Agent Engineer:** (Placeholder outlining logic: If `USER_REJECTED_EDIT`, inform user "Edit cancelled by user.". If `EXECUTION_FAILED...`, inform user "Edit was approved but failed to apply. Error: [details]". No retry in either case for MVP.)

... 