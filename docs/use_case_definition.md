# AI E-commerce Conversion & Shopping Advisor

## 1. Business Problem Statement

The client is a small e-commerce company that wants to increase online revenue by identifying opportunities for improvement across the customer journey.

The company currently has access to website and customer-behaviour data, but this information mainly describes what visitors are doing. The main business challenge is turning these signals into concrete and timely actions.

Potential revenue opportunities may occur when:

- visitors show high purchase intent but do not purchase;
- visitors repeatedly view products without making a decision;
- visitors add products to their cart but abandon the purchase;
- visitors start checkout but do not complete it;
- visitors need assistance choosing between products;
- marketing teams have identified customer segments but do not know which action should be prioritised.

The proposed solution therefore focuses on transforming behavioural signals into actionable recommendations while respecting privacy, consent and human oversight requirements.

---

## 2. Company Profile

### Industry

E-commerce / online retail

### Company Size

Small-to-medium-sized e-commerce business.

### Current State

The company uses website analytics and customer data to understand online activity.

However:

- behavioural data is mainly used for reporting and analysis;
- identifying conversion opportunities requires manual interpretation;
- marketing actions are not necessarily triggered by real-time behavioural signals;
- anonymous visitors cannot be directly contacted individually;
- identified customers can only be contacted through permitted channels when the appropriate consent and legal conditions are satisfied.

The proposed solution is intended to complement existing analytics and marketing tools rather than replace them.

---

## 3. Proposed AI Solution

### Solution Name

**AI E-commerce Conversion & Shopping Advisor**

### Core Proposition

The solution is an AI-powered decision-support and customer-assistance system that analyses permitted customer-journey signals and recommends the most appropriate next action to improve conversion and revenue.

The system combines:

1. behavioural analysis;
2. visitor classification;
3. purchase-intent scoring;
4. funnel-stage detection;
5. AI-generated recommendations;
6. an AI shopping assistant;
7. privacy and consent controls.

The system does not attempt to identify anonymous visitors.

Instead, it distinguishes between:

- anonymous visitors;
- identified visitors;
- identified visitors with appropriate marketing consent.

---

# 4. Customer Journey Logic

The system analyses behavioural signals such as:

- product views;
- number of products viewed;
- product/category interactions;
- time spent on relevant pages;
- returning visits;
- add-to-cart events;
- checkout initiation;
- checkout abandonment;
- purchase events;
- interaction with the AI shopping assistant.

The system then determines the most relevant customer-journey context.

Example:

```text
Behavioural signals
        ↓
Funnel stage
        ↓
Behavioural segment
        ↓
Purchase-intent score
        ↓
Reason
        ↓
Recommended next action

The AI should focus on observable commercial behaviour and should not infer sensitive personal characteristics.

5. Anonymous Visitor Experience

Anonymous visitors can still generate useful behavioural signals without being directly identified.

For example:

Anonymous session
        ↓
Viewed several products
        ↓
Returned to the website
        ↓
High product interest detected
        ↓
AI shopping assistance offered
First intervention

When the configured behavioural conditions are met, the website can automatically display an on-site assistance prompt such as:

"Need help choosing the right product? Our AI shopping assistant can help."

The visitor can choose whether to interact with the assistant.

AI Shopping Assistant

The assistant can:

answer product questions;
ask the visitor about their needs;
compare available products;
explain product differences;
recommend products from the available product catalogue.

The interface clearly identifies the assistant as AI.

If the anonymous visitor does not purchase

The system does not attempt to identify the person.

Instead, the behavioural information can contribute to:

anonymous behavioural segmentation;
aggregate customer-journey analysis;
future marketing campaign planning;
identification of common conversion problems.

Individual outbound email or SMS activation is not performed for an unidentified visitor.

6. Identified Visitor Experience

When a visitor is legitimately identified, for example through an account or an existing customer relationship, the system can use permitted customer and behavioural information relevant to the use case.

The system can detect situations such as:

high purchase intent without purchase;
cart abandonment;
checkout abandonment;
repeated product visits;
product uncertainty;
returning visitors who have not purchased.

The AI then generates a structured recommendation.

Example:

{
  "visitor_type": "identified",
  "funnel_stage": "checkout_abandonment",
  "segment": "high_intent_abandoner",
  "intent_score": 91,
  "reason": "Visitor added a product to cart and initiated checkout but did not complete the purchase.",
  "recommended_action": "cart_recovery_email"
}
7. Next-Best-Action Engine

The core business capability is the Next-Best-Action recommendation.

The AI can recommend actions such as:

offer AI shopping assistance;
recommend a product comparison;
display relevant on-site assistance;
prepare a cart-recovery email;
prepare a customer message;
create a CRM follow-up task;
classify the visitor into a marketing segment;
recommend that no action be taken.

The AI recommendation is based on behavioural evidence and business rules.

The LLM does not independently decide whether a customer may legally be contacted.

Consent, eligibility and other applicable controls are checked by the workflow before an outbound marketing action can occur.

8. Marketing Activation

For identified visitors, outbound marketing actions are only considered when the required consent and legal conditions are satisfied.

The architecture separates:

AI recommendation
        ↓
Consent / eligibility check
        ↓
Approved?
   ┌────┴────┐
   YES       NO
    ↓         ↓
Activation   No outbound
             marketing

Potential activation channels include:

email;
customer messaging;
CRM task;
other approved marketing channels.

For the MVP, outbound actions may be simulated or require human approval rather than being automatically sent to real customers.

9. AI Shopping Assistant

The AI Shopping Assistant is a second core capability of the MVP.

It is designed to help visitors make product decisions.

The visitor may ask:

"Which product is best for my needs?"
"What is the difference between these two products?"
"Which one is better for a beginner?"
"What should I choose if my budget is €100?"

The assistant should ground product recommendations in an approved product catalogue or knowledge base.

It should not invent products, prices, specifications or availability.

The assistant will clearly disclose that the visitor is interacting with an AI system.

10. Key Stakeholders
Stakeholder	Interest
E-commerce owner / CEO	Increase revenue and conversion
Marketing manager	Improve campaign targeting and customer activation
E-commerce manager	Reduce funnel abandonment and improve customer experience
Sales / customer service team	Help customers choose products and recover opportunities
Data / AI team	Ensure reliable AI recommendations and monitoring
IT team	Integrate analytics, website and business systems
DPO / Privacy lead	Ensure GDPR, ePrivacy and data-governance compliance
Customers / visitors	Receive useful assistance without inappropriate profiling or unwanted communications
11. Success Criteria

The MVP will be considered successful if it can demonstrate the following measurable outcomes.

Business outcome 1 — Opportunity detection

The system should correctly classify predefined synthetic customer scenarios into relevant behavioural segments and identify the appropriate funnel stage.

Target:

at least 80% correct classification on the project's validation test scenarios.

This target applies to the MVP test dataset and is not presented as production model performance.

Business outcome 2 — Action recommendation

For predefined scenarios, the system should generate an appropriate next-best-action recommendation based on the available behavioural evidence.

Target:

at least 80% of validation scenarios receive an action judged appropriate against predefined expected outcomes.
Business outcome 3 — Customer assistance

The AI Shopping Assistant should successfully provide product recommendations based on the available product catalogue without inventing unavailable products or unsupported product characteristics.

Target:

90%+ of test recommendations should be grounded in the available product catalogue.
Business outcome 4 — Privacy-aware activation

The workflow must prevent outbound marketing activation when the required marketing consent is absent.

Target:

100% of negative-consent test scenarios must block the outbound marketing action.
12. Out-of-Scope

The following capabilities are explicitly outside the MVP scope.

Identity resolution

The system will not attempt to identify anonymous visitors or discover their identity.

Sensitive profiling

The system will not infer sensitive personal characteristics such as:

health status;
religion;
political opinions;
ethnicity;
sexual orientation;
financial vulnerability;
other sensitive characteristics.
Biometric processing

The MVP will not use:

facial recognition;
biometric identification;
emotion recognition;
biometric categorisation.
Fully autonomous marketing

The MVP will not independently decide to send marketing communications without the required eligibility and consent checks.

Real customer data

The project will use public or synthetic data only.

No real client personal data will be used for the demonstration.

Advertising platform automation

Direct integration with Meta Ads, Google Ads or other advertising platforms is outside the initial MVP.

These integrations may be considered during a future pilot.

Full CDP implementation

A complete Customer Data Platform is outside the MVP.

The architecture will demonstrate how such an event layer could be integrated in a production environment.

Revenue forecasting

The MVP will not attempt to provide long-term revenue forecasting.

The focus is on detecting opportunities and recommending next actions.

13. GDPR and Privacy-by-Design Principles

The solution is designed around the following principles:

data minimisation;
purpose limitation;
consent-aware activation;
separation of anonymous and identified visitors;
avoidance of unnecessary personal data sent to the LLM;
appropriate retention limits;
transparency toward visitors;
support for data-subject rights;
appropriate third-party processor arrangements;
appropriate safeguards for international data transfers.

Only information required for the specific AI task should be sent to the LLM.

For example, the model should preferably receive behavioural context such as:

Product category: Running shoes
Products viewed: 3
Add to cart: Yes
Checkout started: Yes
Purchase: No
Intent score: 91

rather than unnecessary personal information such as a full name, address or phone number.

14. EU AI Act Transparency

The AI Shopping Assistant directly interacts with website visitors.

The interface will therefore clearly indicate that the visitor is interacting with an AI system, in accordance with the applicable AI Act transparency requirements.

Example:

"You are interacting with an AI shopping assistant."

The system is not designed to perform biometric identification, biometric categorisation or emotion recognition.

The AI is used primarily for customer assistance and business decision support.

15. Human Oversight

For the MVP, AI recommendations are treated as decision-support outputs.

A human business user remains responsible for approving sensitive or consequential business actions.

For outbound marketing, the recommended architecture is:

Behaviour
    ↓
AI analysis
    ↓
Recommended action
    ↓
Consent / eligibility rules
    ↓
Human approval where required
    ↓
Activation

This approach reduces the risk of inappropriate automated communications and makes the system easier to monitor.

16. Evolution from Round 1

Round 1 focused on identifying where potential revenue was being lost across the e-commerce customer journey.

The initial concept was an AI-powered revenue optimization advisor capable of identifying opportunities and recommending actions such as:

cart recovery;
campaign optimization;
product personalization;
customer-experience improvements.

During the development of the concept, the use case was refined.

The Round 2 MVP focuses on one central capability:

Detect customer-journey opportunities and recommend the next best action, while providing an AI shopping assistant when customer assistance could improve conversion.

The solution now explicitly separates anonymous and identified visitors.

Anonymous visitors are not individually targeted through email or other identity-based outbound marketing. Instead, the system can provide on-site assistance and generate behavioural segments or aggregate insights.

Identified visitors may receive recommended outbound actions only when the relevant consent and eligibility conditions are satisfied.

This refinement makes the solution more realistic from both a technical and privacy perspective.

17. MVP Definition

The Round 2 MVP will demonstrate an end-to-end flow:

Synthetic visitor event
        ↓
Behaviour analysis
        ↓
Anonymous / identified classification
        ↓
Funnel-stage detection
        ↓
Behavioural segment
        ↓
Intent score
        ↓
Reason
        ↓
Next-best-action recommendation
        ↓
Consent / eligibility check
        ↓
On-site AI assistance
or
Approved activation recommendation

The MVP will demonstrate that the core AI capability actually runs and produces structured, actionable outputs.

The system is intentionally limited in scope so that one complete end-to-end capability can be demonstrated reliably.