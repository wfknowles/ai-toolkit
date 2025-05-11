# Brainstorming Report: Defining Formulas, Analyses, and Agent Tools for AI Budgeting UX

**Version:** 5.0 (Formulas & Tools Focus)
**Date:** 2025-05-04
**Author:** AI Facilitator (Simulated)
**Based on:** Simulated brainstorming session building on previous reports (`budgeting/02/brainstorm.md`, `post-mortem-finance-ux-test-1.md`) with 10 expert personas, focusing on defining specific quantitative elements and agent tools.

*Thesis-quality research paper detailing the definition of key financial formulas, data analyses, and AI agent tool prompts identified as crucial for enhancing the user experience of an AI-driven personal finance application, grounded in a $2600 bi-weekly income scenario.*

---

## 1. Introduction: Operationalizing AI for Financial Insight

Building upon prior brainstorming that established the concept of an expert-configurable AI financial counseling tool tailored to specific user scenarios (e.g., $2600 bi-weekly income), this report details a focused session aimed at defining the *specific operational components* required. The goal was to move from high-level concepts to concrete definitions of the financial formulas, data analysis techniques, and AI agent \"tool\" prompts necessary to deliver tangible value and an unparalleled user experience. Leveraging insights from the successful initial user interaction documented in the `Post Mortem Report`, this session prioritized elements that provide clear, quantitative feedback and enable user interaction via AI agents.

This document synthesizes the outputs of a simulated brainstorming session involving technical, product, UX, and financial experts, focused on defining these core quantitative and agentic building blocks.

---

## 2. Methodology: Focused Brainstorming on Components

The methodology followed previous structures but focused the discussion on specific components:

1.  **Persona Definition:** Utilized the 10-expert panel (PE, Arch, SSE, PO, UX, AgentEng, CPA, CFO, Counselor, FinAnalyst).
2.  **Prerequisite Review & Targeted Concept Generation:** Personas reviewed the `Brainstorm Report` (v4.0) and `Post Mortem Report` (v1.0), then generated concepts specifically defining formulas, analyses, and agent tool prompts (placeholders created in `budgeting/03/pre-analysis/`).
3.  **Component-Focused Pre-Planning:** The facilitator analyzed the concepts, grouping them into Formulas, Analyses, and Agent Tool Prompts, identifying key definitions, dependencies (e.g., data needed for formulas), and potential implementation challenges.
4.  **Simulated Group Discussion (Component Focus):** A multi-round discussion (transcript saved to `sme-group-interview.md` in `budgeting/03`) centered on:
    *   Defining essential **Formulas** (inputs, calculation, value).
    *   Specifying key **Analyses** (data source, method, output).
    *   Brainstorming and structuring **Agent Tool Prompts** (purpose, inputs, expected LLM output).
    *   Selecting and refining the top concepts in each category for MVP and near-term roadmap.
5.  **Synthesized Reporting:** This report documents the defined components.

---

## 3. Defined Core Financial Formulas

The discussion prioritized formulas providing foundational financial health metrics, calculated using the $2600 bi-weekly scenario context and minimal viable user input.

*   **3.1. Disposable Income Calculation:**
    *   **Formula:** `Estimated Monthly Disposable Income = Monthly Net Income - Sum(Known Fixed Monthly Costs)`
    *   **Inputs:** Monthly Net Income (derived from $2600 bi-weekly = ~$5670), User-confirmed Fixed Costs (Mortgage, Child Support, Ortho, essential others).
    *   **Value:** Establishes the core amount available for budgeting variable expenses and savings.
    *   **Implementation:** Backend service, requires precise decimal math.

*   **3.2. Savings Rate Calculation:**
    *   **Formula:** `Monthly Savings Rate = (Net Change in Savings Balances + Explicit Savings Transfers) / Monthly Net Income`
    *   **Inputs:** Monthly Net Income (~$5670), Plaid data for linked savings accounts, potentially user tags for savings transfers.
    *   **Value:** Tracks progress towards accumulation goals as a percentage of income.
    *   **Implementation:** Requires reliable identification of savings accounts/transfers. AI could assist identification.

*   **3.3. Debt-to-Income (DTI) Ratio Calculation:**
    *   **Formula:** `DTI = Total Monthly Debt Payments / Estimated Gross Monthly Income`
    *   **Inputs:** User-provided Monthly Debt Payments (Mortgage, Child Support, Loan Mins, CC Min), Estimated Gross Monthly Income (GMI - requires estimation from $2600 Net, e.g., `Net / (1-EstTaxRate)`).
    *   **Value:** Standard measure of debt load.
    *   **Implementation:** Calculation straightforward, but GMI estimation introduces uncertainty. Caveats must be displayed (UX).

*   **3.4. Budget vs. Actual Variance Calculation:**
    *   **Formula:** `Variance = Actual Spending (Category) - Budgeted Amount (Category)`
    *   **Inputs:** Budgeted amounts (from expert config applied to Disposable Income), Actual Spending (from categorized Plaid data).
    *   **Value:** Core feedback loop for budget adherence.
    *   **Implementation:** Requires accurate categorization and budget generation. Displayed as $ and %.

*   **3.5. Required Savings Rate (Goal-Based):**
    *   **Formula:** `Required Monthly Savings = GoalAmount / MonthsRemaining`
    *   **Inputs:** User/Expert defined Goal Amount & Target Date.
    *   **Value:** Translates future goals into present-day action targets within the $5670 budget context.
    *   **Implementation:** Simple calculation, often used within goal-setting tools/prompts.

*   **3.6. Emergency Fund Coverage Ratio:**
    *   **Formula:** `Coverage (Months) = Liquid Assets (Cash + Savings Balances) / Average Monthly Essential Expenses`
    *   **Inputs:** Linked account balances, estimate of *essential* monthly expenses (subset of total expenses).
    *   **Value:** Measures safety net against income disruption.
    *   **Implementation:** Requires defining/estimating 'essential' expenses.

---

## 4. Defined Core Financial Analyses

These analyses leverage Plaid data and calculated formulas to provide deeper insights.

*   **4.1. Cash Flow Visualization:**
    *   **Technique:** Time-series chart (e.g., weekly bars) plotting income deposits ($2600 events) against aggregated daily/weekly total spending.
    *   **Data Source:** Plaid transaction dates/amounts.
    *   **Value:** Highlights income/expense timing mismatches, potential low-balance periods.
    *   **Implementation:** Frontend charting component using processed transaction data.

*   **4.2. Spending Anomaly Detection (Statistical):**
    *   **Technique:** Calculate historical mean and standard deviation of spending per category (e.g., monthly over 3-6 months). Flag current periods where `Spending > Mean + (X * StdDev)`. `X` is sensitivity parameter (e.g., 1.5-2.0), potentially expert-configurable.
    *   **Data Source:** Historical categorized Plaid transactions.
    *   **Value:** Identifies statistically unusual spending that might indicate issues or require attention, beyond simple budget limits.
    *   **Implementation:** Backend analysis service, likely asynchronous job. Requires sufficient history.

*   **4.3. Subscription Audit (Plaid-based):**
    *   **Technique:** Identify recurring transactions with similar names/amounts suggesting subscriptions. Aggregate total monthly cost.
    *   **Data Source:** Plaid transaction history (names, amounts, dates).
    *   **Value:** Surfaces potentially forgotten/unwanted recurring costs for savings opportunities.
    *   **Implementation:** Pattern matching logic in backend service, presented via Agent Prompt Tool (5.3).

*   **4.4. Debt Payoff Simulation (Snowball/Avalanche):**
    *   **Technique:** Model debt repayment using either Snowball (lowest balance first) or Avalanche (highest interest rate first) method. Calculate time-to-zero and total interest paid for comparison.
    *   **Data Source:** User-provided debt details (balances, interest rates, minimum payments), potential extra payment amount.
    *   **Value:** Helps user choose optimal debt repayment strategy.
    *   **Implementation:** Calculation engine service. Requires debt interest rates for Avalanche.

*   **4.5. Spending Trend Analysis:**
    *   **Technique:** Calculate moving averages (e.g., 3-month) for spending in key categories or overall. Visualize trends.
    *   **Data Source:** Historical categorized Plaid transactions.
    *   **Value:** Helps identify gradual shifts in spending habits.
    *   **Implementation:** Backend analysis service, frontend charting.

---

## 5. Defined Agent Tool Prompts

These represent specific tasks an AI agent could perform using LLMs, often in conjunction with calculation services.

*   **5.1. Metric Explanation Tool:**
    *   **Purpose:** Explain a calculated financial metric simply.
    *   **Inputs:** `Metric Name`, `Metric Value`, `User Context` (e.g., income, goals).
    *   **Agent Action:** Call Prompt Service with inputs.
    *   **Example LLM Output:** \"Your Debt-to-Income (DTI) ratio is 29.1%. This compares your required monthly debt payments to your estimated gross income. Lower is generally better, and below 36% is considered good by many lenders, so you\'re in a healthy range.\"

*   **5.2. Spending Anomaly Explanation Tool:**
    *   **Purpose:** Explain why a spending period was flagged as anomalous.
    *   **Inputs:** `Category`, `Anomalous Spending Amount`, `Historical Average`, `Historical StdDev`.
    *   **Agent Action:** Call Prompt Service with inputs.
    *   **Example LLM Output:** \"Heads up! Your $150 spending on Dining Out this week was flagged because it\'s quite a bit higher than your usual weekly average of $75 (plus or minus about $20). Was there a special occasion?\"

*   **5.3. Subscription Review Interaction Tool:**
    *   **Purpose:** Present potential subscriptions found by analysis (4.3) and get user feedback.
    *   **Inputs:** `List of Potential Subscriptions` (Vendor, Amount, Frequency).
    *   **Agent Action:** Call Prompt Service with list.
    *   **Example LLM Output:** \"I found these potential recurring payments that might be subscriptions: [List formatted]. Are these all active and providing value? Perhaps review if any can be cancelled to save money?\"

*   **5.4. Goal Feasibility Check Tool:**
    *   **Purpose:** Assess if a savings goal is realistic given current finances.
    *   **Inputs:** `Goal Amount`, `Goal Deadline`, `Calculated Monthly Disposable Income`, `Calculated Current Savings Rate`.
    *   **Agent Action:** Call Calculation Service for `Required Monthly Savings`. Feed results & context to Prompt Service.
    *   **Example LLM Output:** \"To save $[Goal Amount] by [Deadline], you\'d need to save about $[Required Rate] per month. Currently, your savings rate suggests you\'re saving around $[Current Savings]/month. This goal looks [challenging] with your current budget. Would you like to explore ways to increase savings?\"

*   **5.5. Budget Adjustment Suggestion Tool:**
    *   **Purpose:** Suggest ways to meet a savings shortfall.
    *   **Inputs:** `Savings Shortfall Amount`, `User Spending Data` (variable categories), `Expert Config` (priorities/limits).
    *   **Agent Action:** Call Prompt Service (potentially with complex logic/rules).
    *   **Example LLM Output:** \"To free up $[Shortfall] for your goal, consider reducing [Category 1] by $[Amt1] or [Category 2] by $[Amt2]. Based on [Expert]\'s priorities, focusing on [Category 1] might be preferable. What do you think?\"

---

## 6. Conclusion & Next Steps

This focused brainstorming session successfully defined a core set of specific financial formulas, data analyses, and agent tool prompts crucial for building an effective and quantitatively grounded AI personal finance assistant. By operationalizing the concepts from previous brainstorms into these concrete components, we establish a clear technical path forward.

The defined elements prioritize providing users with objective financial metrics, actionable insights derived from their data (especially Plaid transactions), and interactive tools accessible via an AI agent interface. The emphasis remains on using AI strategically – primarily for explanation, pattern recognition (anomalies, subscriptions), and facilitating user interaction, while relying on dedicated services for core calculations.

Next steps involve:

1.  Prioritizing these defined formulas, analyses, and agent tools for MVP implementation based on user value and technical feasibility (leveraging the PO/FinAnalyst/SSE perspectives).
2.  Designing the specific database schemas and service APIs (Arch/SSE) to support the required data inputs and outputs.
3.  Implementing the backend calculation services and agent tool functions (SSE).
4.  Developing the corresponding user interface components for data input, visualization, and agent interaction (UX).
5.  Crafting and testing the specific prompt templates for the defined agent tools (PE).

Focusing development on these well-defined quantitative components will accelerate progress towards creating a truly insightful and helpful personal finance UX.

---

## 7. Citations

*   Internal brainstorming concepts: Placeholders in `brain/knowledge/chronological/2025/05/04/brainstorm-tools/budgeting/03/pre-analysis/[Persona Name].md`
*   Simulated group interview transcript: `brain/knowledge/chronological/2025/05/04/brainstorm-tools/budgeting/03/sme-group-interview.md`
*   Prerequisite Brainstorm Report: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/04/brainstorm-tools/budgeting/02/brainstorm.md`
*   Prerequisite Post Mortem Report: `/Users/willknowles/.wfkAi/brain/knowledge/chronological/2025/05/04/post-mortem-finance-ux-test-1.md`
*   (Consider adding citations for specific financial formulas or analysis techniques if needed for formal documentation). 