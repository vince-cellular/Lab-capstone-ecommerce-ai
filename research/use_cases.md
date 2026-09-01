# AI Use Cases

## Core Business Problem

The proposed client is a French e-commerce SME looking to improve conversion and revenue.

The central business question is:

> Where are potential revenue opportunities being lost across the customer journey, and what data-driven actions should the company investigate to improve conversion and revenue?

The proposed solution is an **AI-Powered E-commerce Revenue Optimization Advisor**.

The advisor would analyse available customer-session and e-commerce data, identify patterns associated with non-conversion or stronger conversion, and recommend potential actions for human review.

---

## Initial Use Cases

### Use Case 1 — AI Marketing & Conversion Optimization Advisor

**Objective**

Identify traffic sources and customer behaviours associated with stronger or weaker conversion outcomes and generate recommendations for marketing investigation.

**Potential AI role**

- Analyse conversion patterns by traffic type and visitor characteristics.
- Identify segments or traffic sources with relatively weak conversion.
- Highlight unusual or potentially underperforming patterns.
- Generate data-grounded recommendations for further investigation.

**Business value**

- Improve understanding of acquisition quality.
- Support better targeting decisions.
- Improve conversion efficiency.
- Help marketing teams prioritize areas for testing.

**Dataset fit**

The selected dataset contains `TrafficType`, visitor information and the `Revenue` outcome.

However, it does not contain advertising spend or campaign-level costs.

Therefore, the solution cannot claim to calculate advertising waste or ROAS from this dataset.

**Round 1 feasibility:** High

**Round 2 MVP potential:** High

---

### Use Case 2 — AI Cart / Revenue Recovery Advisor

**Objective**

Identify customer-session behaviours associated with non-conversion and recommend potential recovery actions.

**Potential AI role**

- Identify high-engagement sessions that did not result in revenue.
- Analyse behavioural indicators associated with conversion.
- Prioritize potential revenue-recovery opportunities.
- Generate recommended interventions for human review.

**Business value**

- Potentially improve conversion.
- Identify high-intent non-converting sessions.
- Support customer re-engagement strategies.
- Create a direct connection between behavioural analysis and revenue opportunity.

**Dataset fit**

The dataset provides session-level behavioural variables and a `Revenue` outcome.

However, it does not contain explicit cart events or actual recovery actions.

Therefore, the capstone can identify behavioural patterns associated with non-conversion but cannot claim to measure actual cart abandonment or recovered revenue.

**Round 1 feasibility:** High

**Round 2 MVP potential:** Very High

---

### Use Case 3 — AI Product Discovery & Personalization Advisor

**Objective**

Identify behavioural patterns that could support more relevant product discovery and personalized experiences.

**Potential AI role**

- Analyse product-related page engagement.
- Identify behavioural patterns associated with successful purchases.
- Recommend areas where personalization or product discovery could be investigated.

**Business value**

- Potentially improve product discovery.
- Support conversion improvement.
- Support more relevant customer experiences.

**Dataset fit**

The dataset contains product-related page activity and duration.

However, it does not contain detailed product-level information or individual product identities.

This limits the ability to build a true product recommendation engine from the selected dataset.

**Round 1 feasibility:** Medium

**Round 2 MVP potential:** Medium

---

### Use Case 4 — AI Customer Experience & Support Advisor

**Objective**

Use AI to improve customer-support efficiency and identify customer issues requiring human intervention.

**Potential AI role**

- Classify customer requests.
- Generate draft responses.
- Identify cases requiring escalation.
- Summarize customer interactions.

**Business value**

- Reduce repetitive support work.
- Improve response speed.
- Support customer experience.
- Allow human agents to focus on complex cases.

**Dataset fit**

The selected dataset does not contain customer-support conversations, tickets, response times or satisfaction data.

A separate dataset would therefore be required to demonstrate this use case properly.

**Round 1 feasibility:** Low to Medium

**Round 2 MVP potential:** Medium

---

# Use Case Evaluation

| Use Case | Business Value | Dataset Fit | Dashboard Fit | n8n POC | Round 2 MVP | Overall |
|---|---|---|---|---|---|---|
| AI Marketing & Conversion Optimization | High | High | Very High | High | High | **Strong** |
| AI Cart / Revenue Recovery | Very High | High | Very High | High | Very High | **Strongest** |
| AI Product Discovery & Personalization | High | Medium | High | Medium | Medium | **Promising** |
| AI Customer Experience & Support | High | Low | Medium | High | Medium | **Limited with current dataset** |

---

# Recommended Round 1 Focus

The initial four use cases were considered during the research phase.

Based on the available public dataset and the Round 1 requirements, the strongest candidates are:

1. **AI Marketing & Conversion Optimization**
2. **AI Cart / Revenue Recovery**
3. **AI Product Discovery & Personalization**

The Customer Experience & Support use case is not selected as a primary Round 1 use case because the selected dataset does not contain customer-support data.

The final Round 1 presentation should focus primarily on the first two use cases, with Product Discovery & Personalization presented as an additional opportunity if the available dashboard and data support it.

---

# Proposed AI Solution

The three selected opportunities can be viewed as components of one broader solution:

## AI-Powered E-commerce Revenue Optimization Advisor

The advisor does not automatically decide what the company should do.

Instead, it follows this logic:

Customer / session data

↓

Data analysis

↓

Identify potential revenue opportunity

↓

Explain the evidence

↓

Generate recommended action

↓

Human business review

Possible recommendations include:

- Investigate traffic targeting.
- Test a different customer engagement strategy.
- Investigate high-exit product journeys.
- Consider a recovery or re-engagement intervention.
- Investigate opportunities for personalization.

The recommendation must remain grounded in the available data.

---

# Key Limitation

The public dataset is a proxy and does not represent the fictional client's actual company data.

The proposed solution therefore demonstrates the **method and potential value**, rather than claiming that the identified patterns represent Chleo's actual business performance.

In a real implementation, the same approach would connect to the client's own analytics, transaction, marketing and customer data.