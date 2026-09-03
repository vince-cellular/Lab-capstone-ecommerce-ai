# Business Impact & ROI Framework

## 1. Business Problem

E-commerce businesses receive visitors with different levels of purchase intent, but many visitors leave without completing a purchase.

Traditional recovery approaches can treat visitors too uniformly. They may also trigger communication without sufficiently considering visitor behavior, identification status, marketing consent, or whether a purchase has already been completed.

The POC addresses this problem by using behavioral session data to determine the most appropriate next action for each visitor.

## 2. AI Solution

The POC analyzes visitor session data including:

* Visitor identification status
* Marketing consent
* Returning visitor status
* Pages viewed
* Product views
* Time spent on product pages
* Cart activity
* Checkout activity
* Purchase status
* Product questions
* Email availability

GPT-5-mini produces a structured decision containing:

* Recovery risk
* Main behavioral signal
* Recommended action
* Personalized customer message
* Recommended channel

The n8n workflow then routes the decision to the appropriate action.

Possible outcomes include:

**On-site assistance →** immediate assistance while the visitor is active.

**Email recovery →** used when the visitor is identified, marketing consent is available, and the behavioral evidence supports recovery.

**No recovery action →** used when intervention is unnecessary, including after a completed purchase.

## 3. Expected Business Benefits

The POC is designed to create value through:

### Increased conversion opportunities

High-intent visitors can receive assistance before leaving the website.

### Improved cart and checkout recovery

Visitors who add products to their cart or start checkout can receive an appropriate recovery intervention.

### More relevant customer engagement

The AI uses behavioral evidence to select an action instead of applying the same intervention to every visitor.

### Reduced unnecessary communication

Consent and purchase status are considered before recommending email recovery.

### Automation of recovery decisions

The workflow can analyze sessions and route actions automatically without requiring manual intervention for every visitor.

## 4. Business KPIs

The production pilot should measure the following KPIs:

| KPI                      | Purpose                                                     |
| ------------------------ | ----------------------------------------------------------- |
| Conversion Rate          | Measure completed purchases                                 |
| Cart Recovery Rate       | Measure recovered abandoned carts                           |
| Checkout Completion Rate | Measure visitors completing checkout                        |
| Revenue per Visitor      | Measure commercial value                                    |
| AI Intervention Rate     | Measure how often the AI triggers an action                 |
| Email Recovery Rate      | Measure conversions following email recovery                |
| On-site Conversion Rate  | Measure conversions following on-site assistance            |
| Cost per AI Intervention | Measure AI operating efficiency                             |
| Incremental Revenue      | Measure additional revenue attributable to the intervention |

## 5. ROI Measurement

The basic ROI calculation for a production pilot is:

**ROI = (Incremental Revenue − AI Program Cost) / AI Program Cost × 100**

Where:

**Incremental Revenue = Revenue from treatment group − Expected revenue without AI intervention**

The comparison should be based on a control group rather than simply comparing total revenue before and after implementation.

## 6. Recommended Pilot Design

A controlled A/B test should be used before full production deployment.

### Control Group

Visitors receive the existing e-commerce experience without AI intervention.

### Treatment Group

Visitors are analyzed by the AI decision engine and receive the appropriate intervention when the decision criteria are met.

Both groups should be measured over the same period and under comparable traffic conditions.

### Primary Success Metric

The primary success metric should be **incremental conversion rate**.

Secondary metrics should include:

* Incremental revenue
* Cart recovery rate
* Checkout completion
* Customer engagement
* AI intervention rate
* Cost per recovered customer
* Cost per incremental conversion

## 7. Example ROI Scenario

The following is an illustrative scenario and is **not a measured result from the POC**.

Assume a pilot generates:

* 10,000 eligible visitor sessions
* €50 average order value
* 2.0% baseline conversion rate
* 2.3% treatment conversion rate

Baseline purchases:

**10,000 × 2.0% = 200 purchases**

Treatment purchases:

**10,000 × 2.3% = 230 purchases**

Incremental purchases:

**230 − 200 = 30**

Illustrative incremental revenue:

**30 × €50 = €1,500**

If the AI program cost for the same period were €400:

**ROI = (€1,500 − €400) / €400 × 100 = 275%**

This example demonstrates how ROI could be measured. It should not be presented as actual POC performance.

## 8. Success Criteria

A production pilot should be considered successful if it demonstrates:

1. Positive incremental conversion impact.
2. Positive incremental revenue after AI operating costs.
3. Acceptable AI decision quality.
4. Low hallucination and groundedness risk.
5. Compliance with marketing consent requirements.
6. Acceptable latency for real-time visitor assistance.
7. Sustainable cost per AI intervention.
8. No significant deterioration in customer experience.

## 9. Limitations

The current POC has not yet established a statistically validated conversion uplift.

The LangSmith Playground evaluation also exposed an integration/mapping limitation between the evaluation target and the production n8n prompt. Therefore, the initial automated evaluator scores should not be interpreted as measured production AI performance.

A larger evaluation dataset and a controlled production A/B test are required before making quantitative claims about conversion uplift or ROI.

## 10. Business Conclusion

The POC demonstrates the technical feasibility of using AI to analyze e-commerce visitor behavior and automatically select an appropriate recovery action.

The next business step is not simply to deploy the system at scale, but to run a controlled pilot and measure whether AI interventions generate statistically significant incremental conversions and revenue that exceed the cost of operating the solution.
