# Site Reliability Engineer SME Interview (Round 2)

**1. Do you see any inherent challenges to defining any assets, strategies, methodologies, or workflows?**
Yes. The main challenge is ensuring that reliability and observability are built into the system from the start. Defining SLIs, SLOs, and error budgets for the MVP is often overlooked. There is also a challenge in making sure monitoring and alerting are actionable and not just noise.

**2. Do you anticipate any areas where there might be friction or hard limits?**
- Monitoring: Ensuring comprehensive and meaningful observability
- Incident response: Establishing clear protocols for outages and degradations
- Scalability: Maintaining reliability as the system grows and changes

**3. If you were to take these definitions and bring it to fruition, what would your solution look like?**
I would define SLIs and SLOs for all critical workflows, set up monitoring and alerting with actionable thresholds, and document incident response procedures. Regular reliability reviews and chaos engineering exercises would be part of the process.

**4. Are there any questions that you feel like need to be asked? Or areas where unknown unknowns exist?**
- What are the reliability targets for the MVP?
- How do we ensure that monitoring evolves with the system?
- What is the process for post-incident reviews and learning?

**5. Do you think the previous analysis had any blindspots?**
Possibly. There may be blindspots around the definition of reliability targets, the integration of observability tools, and the process for continuous improvement.

**6. Do you believe any SMEs have been left out of this round that should attend future rounds based on this specific concept?**
A Monitoring Specialist for advanced observability tooling and a Process Improvement Lead for continuous reliability enhancements. 