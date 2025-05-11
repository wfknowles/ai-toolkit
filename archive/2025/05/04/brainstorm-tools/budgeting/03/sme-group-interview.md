# SME Group Interview - Budgeting Brainstorm (Formulas, Analyses, Agent Prompts Focus)

*Simulated transcript: Focus on defining specific financial formulas, analyses, and agent tool prompts, using prerequisites and $2600 scenario context. Participants: Prompt Engineer (PE), AI Orchestrator Architect (Arch), Senior Software Engineer (SSE), Product Owner (PO), AI UX Engineer (UX), AI Agent Engineer (AgentEng), Certified Public Accountant (CPA), Chief Financial Officer (CFO), Financial Counselor (Counselor), Financial Analyst (FinAnalyst).*

**(Facilitator opens, reviews goal: Define concrete formulas, analyses, and agent tool prompts based on previous brainstorms.)**

---

**Part 1: Key Formulas - Discussion**

*   **Facilitator:** Let's start with core formulas identified in pre-analysis. Financial Analyst, CPA - thoughts on Disposable Income, Savings Rate, DTI, Net Worth, Emergency Fund Ratio?
*   **FinAnalyst:** Disposable Income (`Monthly Net Income - Fixed Costs`) is foundational. Savings Rate (`Savings / Income`) is key for goals. DTI needs careful handling of Gross vs Net income ($2600 is net). Net Worth (`Assets - Liabilities`) requires significant user input beyond Plaid.
*   **CPA:** Agree. For DTI with only $2600 net, we must estimate Gross (`Net / (1-EstTaxRate)`) and state the assumption clearly. Better to get user input for Gross if possible. Emergency Fund Ratio (`Liquid Assets / Monthly Essentials`) needs clear definition of 'Essentials' - maybe start with Fixed Costs + estimate for Food/Transport?
*   **Counselor:** Presenting these needs care. A low Savings Rate or high DTI shouldn't feel like failure. Focus on *tracking change* over time.
*   **SSE:** Implementing these requires validated libraries (`decimal.js`) and clear input DTOs. Net Worth calculation needs careful handling of potentially missing user inputs for assets/liabilities.
*   **PO:** MVP must include Disposable Income calc. Savings Rate and DTI are high value but depend on data quality/inputs. Net Worth likely post-MVP due to input friction.
*   **UX:** Visualizing DTI/Savings Rate needs gauges/trends, not just raw numbers. Need tooltips explaining the calculation simply.

---

**Part 2: Key Analyses - Discussion**

*   **Facilitator:** Moving to analyses: Cash Flow, Budget Variance, Trend Analysis, Statistical Anomaly Detection, Subscription Audit.
*   **FinAnalyst:** Cash Flow Viz (Income vs Spending) is crucial for the $2600 bi-weekly timing. Trend Analysis (moving averages on categories) helps spot habit changes. Anomaly Detection (StdDev) finds outliers budget rules might miss.
*   **CPA:** Budget vs. Actual Variance is standard practice, vital for control. All these depend heavily on accurate Plaid categorization.
*   **PO:** Subscription Audit seems like quick win – high potential savings identified via Plaid data pattern matching.
*   **Arch:** Trend/Anomaly detection likely need dedicated async jobs and potentially time-series data storage separate from main PG DB for performance.
*   **SSE:** Need robust implementation for moving averages, standard deviation calculations over transaction data. Need efficient DB queries.
*   **UX:** Variance needs clear viz (bars showing over/under). Anomaly flags need clear presentation with context (avg vs. current). Subscription list needs easy 'Keep/Cancel' interaction.
*   **AgentEng:** Agents are well-suited to run these analyses periodically (Anomaly, Trends, Subscription Audit) and flag results for user/PE explanation.

---

**Part 3: Agent Tool Prompts - Discussion**

*   **Facilitator:** Let's discuss the agent tool prompts. PE, you proposed explanation, data extraction, feasibility checks, suggestions, simulations.
*   **PE:** Key is structuring prompts with clear inputs/outputs. For explanations, input=[Metric, Value, Context], output=[Simple Text]. For simulations (debt payoff, what-if), input=[Scenario Params, User Data], output=[Projected Outcome Text/Data]. Need to separate calculation logic from LLM explanation generation.
*   **AgentEng:** Agents need a clear way to invoke these prompts via the orchestrator. Need standardized input formats from agent to prompt tool.
*   **Arch:** Requires a 'Prompt Service' that takes structured requests, formats them for the LLM (potentially selecting specific prompt templates), and returns structured responses.
*   **SSE:** Need backend functions corresponding to *actions* agent prompts might suggest (e.g., function to actually *adjust* budget allocation after user confirms suggestion).
*   **UX:** How does user invoke these? Chat? Buttons contextual to data displays? Needs testing. Output needs clear attribution ("AI Assistant calculated...").
*   **Counselor:** Explanation prompts are vital. Suggestion prompts need to reflect configured tone (empathetic vs direct) and avoid being overly prescriptive.
*   **FinAnalyst:** Data extraction prompts need high accuracy for numbers. Simulation prompts need robust underlying calculation models.

---

**Part 4: Synthesis & Selection**

*   **Facilitator:** Okay, let's synthesize. High priority seems to be: Formulas (Disposable Income, Savings Rate, DTI - w/ caveats, Variance), Analyses (Cash Flow Viz, Budget Variance Report, Anomaly Detection, Subscription Audit), Agent Prompts (Metric Explanation, Anomaly Explanation, Subscription Review). What are the absolute essentials for an impactful MVP?
*   **PO:** MVP: Disposable Income calc, Budget Variance calc/display, Cash Flow Viz, Savings Rate calc, Metric Explanation prompt tool, Subscription Audit tool.
*   **FinAnalyst:** Agree, but DTI is standard, include it even with estimation caveats. Anomaly detection adds unique AI value early.
*   **CPA:** Accurate categorization is prerequisite for Variance/Anomaly. Need robust user review flow (UX concept 9).
*   **Counselor:** Metric Explanation and how Variance is framed are crucial for positive UX.
*   **CFO:** Savings Rate and simple Goal Feasibility/Required Savings Rate calc are important for forward view.
*   **(Further discussion refining MVP list, considering dependencies and user value...)**

**Refined Top Concepts (Focus: Formulas, Analyses, Agent Prompts):**

1.  **Formula: Disposable Income Calculation** (Core - FinAnalyst/CPA)
2.  **Formula: Savings Rate Calculation** (Core Metric - FinAnalyst/CPA)
3.  **Formula: DTI Calculation** (Core Metric w/ Caveats - FinAnalyst/CPA)
4.  **Formula: Budget vs. Actual Variance** (Core Control - CPA/FinAnalyst)
5.  **Analysis: Cash Flow Visualization** (Insight - FinAnalyst/UX)
6.  **Analysis: Spending Anomaly Detection (Statistical)** (AI Insight - FinAnalyst/AgentEng)
7.  **Analysis: Subscription Audit (Plaid-based)** (Actionable Savings - PO/FinAnalyst)
8.  **Agent Prompt Tool: Metric Explanation** (Literacy/UX - PE/Counselor)
9.  **Agent Prompt Tool: Spending Anomaly Explanation** (Context/UX - PE/AgentEng)
10. **Agent Prompt Tool: Subscription Review Interaction** (Actionable UX - PE/UX)
11. **(Supporting) Formula: Required Savings Rate (Goal-Based)** (Planning - FinAnalyst/CFO)
12. **(Supporting) Analysis: Debt Payoff Simulation (Snowball/Avalanche)** (Planning/Action - FinAnalyst/CPA)
13. **(Supporting) Data Quality: Categorization Confidence & Review Flow** (Foundation - CPA/SSE/UX)

**(Session concludes with consensus on core formulas, analyses, and agent prompt tools for development focus.)** 