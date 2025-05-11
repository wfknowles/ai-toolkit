# Financial Analyst - Pre-Analysis Concepts

*Initial concepts focusing on specific formulas, quantitative analysis techniques, and data interpretation.*

1.  **Detailed Income Analysis:** Beyond $2600 bi-weekly, analyze income stability/volatility if possible (e.g., standard deviation of deposits if multiple income sources linked via Plaid).
2.  **Expense Trend Analysis:** Formula/Analysis: Calculate moving averages (e.g., 3-month) for key spending categories. Identify categories with statistically significant increasing/decreasing trends.
3.  **Category Spending Ratios:** Formula: `Spending in Category X / Total Monthly Income` (or Total Spending). Compare user's ratios to benchmarks (e.g., typical % for housing, food) or expert-configured targets.
4.  **Subscription Cost Analysis:** Analysis: Identify recurring payments via Plaid. Calculate `Total Monthly Subscription Cost` and `% of Disposable Income`. Prompt user review (PE Tool 6).
5.  **Debt Payoff Optimization Analysis:** Implement both Snowball (lowest balance first) and Avalanche (highest interest rate first) methods. Calculate total interest paid and time-to-freedom for each. Present comparison.
6.  **Emergency Fund Coverage Ratio:** Formula: `Liquid Assets (Cash + Savings Balances) / Average Monthly Expenses`. Calculate and track progress towards 3-6 month goal.
7.  **Sensitivity Analysis (What-If Tool):** Agent tool prompt: "Show impact on my [Savings Goal / Budget Surplus / Debt Payoff Date] if my [Income changes by X% / Expenses in Cat Y increase by $Z / I add $W extra to debt payment]." Requires underlying calculation model.
8.  **Burn Rate Calculation:** Formula: `(Starting Cash Balance - Ending Cash Balance) / Number of Months`. Useful for tracking periods of negative cash flow.
9.  **Data Cleansing Recommendations:** Analyze Plaid data for common issues (duplicate transactions, transfers needing categorization) and suggest automated or manual cleanup steps to improve analysis accuracy. 