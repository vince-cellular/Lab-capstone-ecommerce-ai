# POC Documentation — AI E-commerce Conversion & Shopping Advisor

## 1. POC Overview

### Project

**AI E-commerce Conversion & Shopping Advisor**

### Purpose

The Proof of Concept (POC) demonstrates how an AI system can analyse e-commerce visitor behaviour and recommend an appropriate next action during the customer journey.

The POC connects an e-commerce website frontend to an n8n workflow. Behavioural information is sent to the workflow, analysed by an AI model, and converted into a structured recommendation.

The workflow then applies deterministic business rules before allowing a customer-facing action.

The POC demonstrates two principal intervention paths:

1. **On-site assistance** for visitors who should receive immediate shopping assistance.
2. **Email recovery** for identified visitors who have the required marketing consent and have not purchased.

The POC also demonstrates situations where no outbound marketing action should be performed.

---

# 2. Business Objective

The business objective is to determine whether AI can transform customer behavioural signals into timely and actionable interventions that may improve e-commerce conversion.

The POC focuses on:

* identifying purchase-related behavioural signals;
* detecting cart or checkout abandonment opportunities;
* recommending a next-best action;
* generating a short customer-facing message;
* selecting an appropriate communication channel;
* applying consent and purchase-status controls before marketing activation.

The POC is intended to validate technical feasibility and the core business logic before a production pilot.

---

# 3. Tools Used

| Component            | Tool                             | Purpose                                                                        |
| -------------------- | -------------------------------- | ------------------------------------------------------------------------------ |
| E-commerce frontend  | HTML / JavaScript                | Simulates the customer website and captures visitor behaviour                  |
| Workflow automation  | n8n                              | Receives events, applies business logic and orchestrates actions               |
| AI analysis          | OpenAI GPT-5-mini                | Analyses behavioural data and generates the next-best-action recommendation    |
| AI output parsing    | n8n Code node                    | Converts the structured AI response into workflow fields                       |
| Marketing activation | Gmail / Gmail API integration    | Sends an approved recovery email                                               |
| Web communication    | n8n Webhook / Respond to Webhook | Connects the website frontend with the AI workflow                             |
| MVP                  | Python                           | Provides the separate working application demonstrating the core AI capability |

---

# 4. POC Architecture

The high-level architecture is:

```text
E-commerce Website
        |
        | Visitor behavioural event
        ↓
n8n Webhook
        |
        ↓
Edit Fields
        |
        ↓
AI Analysis — GPT-5-mini
        |
        ↓
Parse AI Decision
        |
        ↓
Consent / Purchase / Channel Rules
        |
        ├───────────────┐
        ↓               ↓
   Email Recovery    On-site Assistance
        |               |
        ↓               ↓
     Gmail        Website Response
```

The architecture intentionally separates AI recommendation from action execution.

The AI recommends an action, but deterministic workflow conditions control whether a marketing action is allowed.

---

# 5. Input Data

The website sends behavioural information to the n8n webhook.

The POC currently processes fields including:

```text
visitor_id
identified
consent_marketing
returning_visitor
pages_viewed
product_views
time_on_product_seconds
added_to_cart
checkout_started
purchased
product_questions
email
```

These fields provide observable information about the customer's interaction with the website.

The system does not require the AI to infer sensitive personal characteristics.

---

# 6. n8n Workflow

## Step 1 — Visitor Event

The website sends a POST request to the n8n webhook:

```text
nova-visitor-event
```

The webhook acts as the entry point for the customer behavioural event.

---

## Step 2 — Edit Fields

The `Edit Fields1` node extracts the relevant information from the webhook payload and creates a clean structure for the AI workflow.

For example:

```text
visitor_id
identified
consent_marketing
returning_visitor
pages_viewed
product_views
time_on_product_seconds
added_to_cart
checkout_started
purchased
product_questions
email
```

This provides the AI model with a consistent input structure.

---

# 7. AI Behavioural Analysis

The `Message a model` node uses **GPT-5-mini** to analyse the customer session.

The AI is instructed to determine:

1. `recovery_risk`
2. `main_signal`
3. `recommended_action`
4. `customer_message`
5. `channel`

The model is explicitly instructed to:

* use only the provided customer data;
* avoid inventing reasons for abandonment;
* avoid inventing discounts or promotions;
* avoid inventing product information;
* avoid claiming that a message has already been sent;
* respect marketing consent;
* avoid cart recovery after purchase;
* base risk on observable behavioural evidence.

The AI must return valid JSON.

Example output:

```json
{
  "recovery_risk": "Medium",
  "main_signal": "Added to cart but did not start checkout",
  "recommended_action": "Send a reminder email with a clear link to resume the cart and an offer of assistance.",
  "customer_message": "Hi — we noticed you added items to your cart but didn't complete checkout. Need any help finishing your order? Reply to this email or return to your cart to continue.",
  "channel": "email"
}
```

---

# 8. Parse AI Decision

The `Parse AI Decision` Code node extracts the JSON returned by the AI model and makes the decision available as normal n8n fields.

The resulting fields are:

```text
recovery_risk
main_signal
recommended_action
customer_message
channel
```

This allows subsequent workflow nodes to make deterministic decisions based on the AI output.

---

# 9. Marketing Eligibility Check

The `If` node checks three conditions before an email can be sent.

### Condition 1 — Recommended channel

The AI must recommend:

```text
channel = email
```

### Condition 2 — Marketing consent

The visitor must have:

```text
consent_marketing = true
```

### Condition 3 — Purchase status

The visitor must not have purchased.

Therefore, the email path is conceptually:

```text
AI recommends email
        AND
Marketing consent = true
        AND
Purchased = false
        ↓
Send email
```

If these conditions are not satisfied, the workflow does not send the recovery email.

This is an important design principle of the POC: **the AI recommends; the workflow controls eligibility.**

---

# 10. Email Recovery Action

When the eligibility conditions are satisfied, the `Send a message` Gmail node sends the customer message to the email address provided in the session data.

The email content is generated by the AI through:

```text
customer_message
```

The POC was successfully tested with an actual email delivery.

The successful Gmail execution returned:

```text
id: 1a0679c5a3bbe99e
threadId: 1a0679c5a3bbe99e
labelIds: UNREAD, SENT, INBOX
```

This confirms that the POC successfully executed the end-to-end recovery path from behavioural event to AI decision to email delivery.

---

# 11. On-Site Assistance Path

The workflow also contains a `Needs On-Site Assistance?` condition.

When the AI recommends:

```text
channel = on-site
```

the workflow follows the on-site path.

The response is returned to the website through the `Respond to Webhook` node.

This allows the frontend to display an appropriate customer-facing assistance intervention.

The purpose of this path is particularly relevant for visitors who are not individually identified and therefore should not receive individual outbound marketing communication.

---

# 12. Anonymous Visitor Logic

For an anonymous visitor, the system can analyse behavioural signals and recommend on-site assistance.

Example conceptual flow:

```text
Anonymous visitor
        ↓
Behavioural signals detected
        ↓
AI analyses behaviour
        ↓
On-site assistance recommended
        ↓
Website receives response
        ↓
Visitor decides whether to interact
```

The POC does not attempt to identify an anonymous visitor in order to send individual marketing communication.

---

# 13. Tested Scenarios

The POC was tested using different combinations of visitor status, consent and purchase status.

### Scenario 1 — On-site assistance

The AI identifies a situation where immediate on-site assistance is appropriate.

Expected behaviour:

```text
AI recommendation
        ↓
channel = on-site
        ↓
Website receives response
        ↓
On-site assistance can be displayed
```

This scenario was successfully tested during development.

---

### Scenario 2 — Identified visitor + marketing consent + no purchase

The visitor is identified and has marketing consent.

The visitor has added items to the cart but has not completed the purchase.

Expected behaviour:

```text
AI recommendation
        ↓
channel = email
        ↓
consent_marketing = true
        ↓
purchased = false
        ↓
Email sent
```

This scenario was successfully tested end to end.

---

### Scenario 3 — Identified visitor without marketing consent

The visitor is identified but does not have marketing consent.

Expected behaviour:

```text
AI may identify a recovery opportunity
        ↓
Marketing consent = false
        ↓
Email blocked
```

The workflow therefore prevents the AI recommendation from directly causing an unauthorised marketing communication.

---

### Scenario 4 — Visitor has already purchased

If:

```text
purchased = true
```

the system should not recommend or execute cart recovery.

Expected behaviour:

```text
Purchased
    ↓
No cart recovery
```

This scenario was tested by changing the test session data.

---

# 14. AI Capability Demonstrated

The POC demonstrates several AI capabilities:

### Behaviour interpretation

The AI interprets multiple behavioural signals rather than relying on a single event.

### Classification

The AI classifies the recovery opportunity as:

```text
Low
Medium
High
```

### Signal detection

The AI identifies the strongest behavioural signal supporting its recommendation.

### Next-best-action recommendation

The AI determines the most appropriate next action based on the available evidence.

### Natural-language generation

The AI generates a short customer-facing message appropriate to the identified situation.

### Channel recommendation

The AI recommends a communication channel such as:

```text
email
on-site
none
unknown
```

---

# 15. What the POC Proves

The POC demonstrates that it is technically feasible to:

* capture customer behavioural events from an e-commerce website;
* send these events to an automation workflow;
* analyse the events using an LLM;
* generate a structured AI decision;
* apply deterministic consent and purchase controls;
* trigger an email recovery action when eligible;
* return an on-site assistance response to the website;
* support different customer scenarios through the same workflow.

The successful email test provides evidence that the complete workflow can execute an actual customer-facing action.

---

# 16. What the POC Does Not Prove

The POC does not yet prove:

* production-scale reliability;
* long-term conversion improvement;
* actual incremental revenue;
* optimal AI accuracy across a large customer population;
* optimal recovery timing;
* optimal behavioural thresholds;
* integration with a production CRM;
* production-grade identity resolution;
* production-grade consent management;
* full monitoring and observability;
* enterprise-scale security;
* full GDPR operational implementation;
* statistically significant business impact.

These elements should be validated during a controlled pilot.

---

# 17. Limitations Compared with Production

The current POC uses a simplified demonstration environment.

A production implementation would require additional capabilities including:

### Data infrastructure

A production event-tracking and customer-data architecture would be required rather than demonstration session data.

### Identity management

Visitor identification would need to use the company's existing authenticated customer or CRM infrastructure.

### Consent management

Production consent status should come from the company's approved consent-management system rather than a manually controlled test value.

### Product catalogue integration

The shopping assistant would need access to an authoritative product catalogue containing current product information.

### CRM integration

Recovery actions could be integrated with the company's CRM and marketing automation platform.

### Monitoring

The production solution would require monitoring of:

* AI decisions;
* workflow failures;
* email delivery;
* customer engagement;
* conversion;
* false positives;
* blocked actions;
* cost and latency.

### Security

Production deployment would require appropriate authentication, access control, secret management and protection of customer data.

---

# 18. Reproduction Instructions

## Prerequisites

The following are required:

* n8n instance;
* OpenAI API credentials;
* Gmail OAuth credentials for the email test;
* local e-commerce frontend;
* browser;
* configured webhook.

---

## Basic Reproduction Flow

### 1. Start the e-commerce frontend

Open the project frontend in the browser.

### 2. Generate a visitor session

Interact with the website by viewing products and performing actions such as adding an item to the cart.

### 3. Send the behavioural event

The frontend sends the session data to the n8n webhook.

### 4. Run the AI analysis

The `Message a model` node analyses the session.

### 5. Parse the response

The `Parse AI Decision` node converts the AI response into structured fields.

### 6. Apply workflow controls

The workflow evaluates:

```text
channel
consent_marketing
purchased
```

### 7. Execute the appropriate action

Depending on the result:

```text
Email
OR
On-site assistance
OR
No marketing action
```

### 8. Verify the response

The workflow returns the AI decision to the website through the webhook response.

---

# 19. Demo Recommendation

For the final presentation, the POC should be demonstrated using one clear end-to-end scenario.

Recommended demonstration:

```text
Visitor adds item to cart
        ↓
Does not complete checkout
        ↓
Behavioural event sent to n8n
        ↓
GPT-5-mini analyses the session
        ↓
AI recommends email recovery
        ↓
Consent = true
        ↓
Purchased = false
        ↓
Email is sent
        ↓
Customer receives recovery message
```

A second scenario can then be shown briefly to demonstrate that the workflow does not send marketing communication when the required conditions are not satisfied.

A recorded backup of the working demonstration should be retained in case of a live-demo failure.

---

# 20. POC Conclusion

The POC validates the core technical concept of the AI E-commerce Conversion & Shopping Advisor.

It demonstrates an end-to-end flow in which observable customer behaviour is transformed into an AI-generated next-best-action recommendation and then processed through deterministic business controls before customer-facing activation.

The most important architectural principle demonstrated by the POC is:

```text
Behaviour
    ↓
AI recommendation
    ↓
Business rules
    ↓
Consent / eligibility
    ↓
Approved action
```

The next stage is not to expand the POC indefinitely, but to validate its business value during a controlled pilot using real customer-journey baselines, measurable conversion outcomes and production-grade privacy, security and monitoring controls.

## 8. AI Evaluation

### Evaluation Dataset

An evaluation dataset named `Ecommerce-AI-Visitor-Decision-Evaluation-v2` was created in LangSmith with 8 representative e-commerce visitor scenarios.

The dataset uses the same input schema as the production n8n POC:

- visitor identification
- marketing consent
- returning visitor status
- pages viewed
- product views
- time on product pages
- cart activity
- checkout activity
- purchase status
- product questions
- email availability

### Evaluation Dimensions

The following LangSmith evaluators were configured:

- Correctness
- Answer Relevance
- Hallucination
- Bias & Fairness

### Evaluation Observation

The initial automated Playground experiment revealed an integration/mapping limitation: the evaluation target did not reproduce the production n8n decision prompt and therefore generated generic responses for some test cases.

Consequently, the resulting evaluator scores were not considered representative of the production POC's AI performance and were not used as performance claims.

The evaluation dataset and evaluator configuration remain available in LangSmith for future iteration.

### Responsible AI Controls

The production POC includes explicit safeguards in the AI system prompt:

- Marketing email is not recommended when `consent_marketing` is false.
- Cart recovery is not recommended when `purchased` is true.
- The model is instructed not to invent products, prices, promotions, availability, or customer information.
- Recovery risk must be based only on provided behavioral evidence.
- Unknown information must be identified as unknown.
- The model must return structured JSON for downstream automation.
