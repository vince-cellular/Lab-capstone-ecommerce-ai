# MVP Documentation — AI E-commerce Visitor Recovery

## 1. MVP Objective

The MVP demonstrates an AI-powered e-commerce visitor analysis and next-best-action workflow.

Its purpose is to show how behavioral signals from an e-commerce visitor can be transformed into an actionable recommendation while applying basic privacy, consent and purchase-status safeguards.

The MVP is intentionally limited in scope. It demonstrates the core capability without attempting to implement a complete production e-commerce platform.

---

## 2. MVP Architecture

The current MVP uses:

* **n8n** — workflow orchestration and automation
* **OpenAI GPT-5-mini** — behavioral analysis and recommendation generation
* **Gmail** — demonstration email activation
* **LangSmith** — AI evaluation and monitoring
* **Synthetic visitor data** — testing without real customer personal data
* **Webhook** — receives visitor-session events from the e-commerce front end

High-level flow:

```text
E-commerce visitor event
        ↓
n8n Webhook
        ↓
Normalize visitor data
        ↓
AI behavioral analysis
        ↓
Structured AI decision
        ↓
Consent / purchase checks
        ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Email        On-site action     No action
        ↓
Response to website
```

---

## 3. Implemented MVP Workflow

### Step 1 — Visitor Event

The workflow receives a visitor event through an n8n webhook.

The event contains behavioral and eligibility information such as:

* visitor ID
* identified status
* marketing consent
* returning visitor status
* pages viewed
* product views
* time spent on product pages
* add-to-cart status
* checkout status
* purchase status
* product questions
* email availability

The MVP uses synthetic test scenarios.

---

## 4. Data Preparation

The webhook data is passed through an n8n field-mapping step.

This creates a normalized structure that can be consumed consistently by the AI model.

Example:

```json
{
  "visitor_id": "eval_007",
  "identified": false,
  "consent_marketing": false,
  "returning_visitor": false,
  "pages_viewed": 8,
  "product_views": 6,
  "time_on_product_seconds": 300,
  "added_to_cart": true,
  "checkout_started": true,
  "purchased": false,
  "product_questions": 2,
  "email": ""
}
```

---

## 5. AI Decision Engine

The normalized visitor data is passed to GPT-5-mini.

The model is instructed to return a structured decision containing:

```json
{
  "recovery_risk": "High",
  "main_signal": "Checkout started without purchase",
  "recommended_action": "Offer cart recovery assistance",
  "customer_message": "I can help if you need assistance completing your checkout.",
  "channel": "on-site"
}
```

The five decision fields are:

### Recovery risk

Classifies the recovery opportunity as:

* Low
* Medium
* High

### Main signal

Identifies the strongest behavioral signal supported by the available data.

### Recommended action

Determines the most appropriate next action.

### Customer message

Generates a short message based only on the available evidence.

### Channel

Selects an appropriate channel such as:

* on-site
* email
* none
* unknown

---

## 6. AI Guardrails

The system prompt contains explicit rules designed to reduce unsupported AI decisions.

The AI is instructed to:

* use only the supplied customer data;
* avoid inventing reasons for abandonment;
* avoid inventing products;
* avoid inventing prices;
* avoid inventing promotions;
* avoid inventing product availability;
* avoid inventing customer information;
* identify unavailable information as unknown;
* avoid marketing email when marketing consent is false;
* avoid cart recovery when a purchase has already occurred;
* base recovery risk on behavioral evidence;
* return structured JSON.

These controls are part of the POC design and should be complemented by deterministic workflow rules in a production implementation.

---

## 7. Decision Parsing

The AI response is parsed by an n8n Code node.

The JSON response is converted into structured fields:

* `recovery_risk`
* `main_signal`
* `recommended_action`
* `customer_message`
* `channel`

These fields are then available to downstream workflow nodes.

---

## 8. Consent and Purchase Controls

The workflow contains deterministic checks after the AI decision.

For an email action to proceed, the workflow checks:

```text
AI recommends email
        AND
marketing consent is true
        AND
purchase has not occurred
        ↓
Email activation
```

If these conditions are not satisfied, the workflow does not send the marketing email.

This separation is important because the LLM recommends an action, while the workflow enforces eligibility conditions.

The LLM is therefore not the final authority for marketing permission.

---

## 9. Email Activation

When the workflow determines that email activation is permitted, the Gmail node can send the generated customer message.

The current implementation is intended as a demonstration of the automation path.

Production deployment would require:

* verified sender infrastructure;
* appropriate email provider configuration;
* consent and legal-basis validation;
* unsubscribe mechanisms where applicable;
* frequency controls;
* monitoring;
* deliverability controls.

---

## 10. On-Site Assistance Path

When the AI recommends an `on-site` channel, the workflow returns the structured recommendation to the website.

Example:

```json
{
  "recovery_risk": "High",
  "main_signal": "Checkout started without purchase",
  "recommended_action": "Offer cart recovery assistance",
  "customer_message": "I can help if you need assistance completing your checkout.",
  "channel": "on-site"
}
```

The front-end can use this response to display an appropriate assistance experience.

For example:

```text
Need help completing your purchase?
Our AI shopping assistant can help.
```

The visitor remains free to interact with the assistant.

---

## 11. Webhook Response

The workflow returns a structured JSON response to the originating application.

This allows the e-commerce front end to consume the AI decision programmatically.

The response contains:

```text
recovery_risk
main_signal
recommended_action
customer_message
channel
```

This creates a separation between:

**AI decision generation**

and

**website presentation / business activation.**

---

## 12. Example Scenarios

### Scenario A — High-intent anonymous visitor

Input characteristics:

* Anonymous
* No marketing consent
* Multiple product views
* Product questions
* Added to cart
* Checkout started
* No purchase

Expected behavior:

```text
High recovery risk
        ↓
Checkout abandonment signal
        ↓
On-site assistance
        ↓
No marketing email
```

---

### Scenario B — Identified visitor without marketing consent

Input characteristics:

* Identified
* Returning visitor
* Email available
* Marketing consent false
* Added to cart
* Checkout started
* No purchase

Expected behavior:

```text
High recovery risk
        ↓
Checkout abandonment signal
        ↓
On-site assistance
        ↓
No marketing email
```

Having an email address does not by itself authorize marketing communication.

---

### Scenario C — Purchased visitor

Input characteristics:

* Added to cart
* Checkout started
* Purchased true

Expected behavior:

```text
Purchase detected
        ↓
No cart recovery
```

This prevents the workflow from recommending recovery for a completed purchase.

---

## 13. Error Handling and Reliability

The MVP currently uses structured AI output and a dedicated parsing step.

A production implementation should additionally include:

* JSON validation;
* retry handling;
* API failure handling;
* timeout handling;
* malformed-response handling;
* fallback decisions;
* logging;
* alerting;
* rate limiting;
* monitoring of workflow failures.

If the AI service is unavailable, the website should continue operating normally rather than blocking the customer journey.

---

## 14. AI Evaluation

An evaluation dataset named:

`Ecommerce-AI-Visitor-Decision-Evaluation-v2`

was created in LangSmith.

The dataset contains representative synthetic e-commerce visitor scenarios covering different behavioral situations.

Evaluation dimensions configured include:

* Correctness
* Answer Relevance
* Hallucination
* Bias / Fairness

The initial automated evaluation revealed an integration/mapping limitation where the evaluation target did not consistently reproduce the production n8n decision prompt.

Therefore, the resulting automated scores are **not presented as evidence of production AI performance**.

The evaluation dataset remains available for future evaluation iterations.

A production evaluation setup should execute the actual production prompt/workflow or an equivalent controlled evaluation harness.

---

## 15. Security and Privacy Scope

The MVP uses synthetic visitor data.

No real customer personal data is required for the demonstration.

The production architecture should implement:

* data minimization;
* purpose limitation;
* access controls;
* encryption;
* retention limits;
* deletion procedures;
* processor agreements;
* transfer safeguards;
* appropriate logging;
* privacy notices.

The AI model should receive only information necessary for the specific decision.

---

## 16. What the MVP Demonstrates

The MVP demonstrates that:

1. Visitor events can be received automatically.
2. Behavioral information can be normalized.
3. An LLM can analyze the visitor journey.
4. The model can produce structured recovery decisions.
5. The system can distinguish different recovery situations.
6. Consent can be enforced through workflow logic.
7. Purchase status can prevent inappropriate recovery actions.
8. The AI decision can be returned to the website.
9. An approved email path can be automated.
10. The architecture can be evaluated using synthetic scenarios.

---

## 17. What the MVP Does Not Prove

The MVP does not prove:

* production ROI;
* actual conversion uplift;
* production-scale performance;
* complete GDPR compliance;
* complete EU AI Act compliance;
* perfect AI accuracy;
* absence of all hallucinations;
* long-term customer acceptance;
* production email deliverability;
* scalability to all e-commerce platforms.

These claims require controlled pilot testing and production-grade validation.

---

## 18. Future Pilot Improvements

Before production deployment, the solution should be extended with:

### Product knowledge

Connect the AI shopping assistant to an approved product catalogue or knowledge base so product recommendations are grounded in actual product information.

### Evaluation

Create an automated evaluation harness that executes the same decision logic used by the production workflow.

### Deterministic controls

Move critical eligibility decisions from the LLM into explicit workflow rules.

### Monitoring

Track:

* AI latency
* token consumption
* API cost
* recommendation quality
* hallucination rate
* recovery conversion
* customer complaints
* intervention frequency

### Experimentation

Use an A/B or controlled pilot design to measure incremental conversion and revenue.

---

## 19. MVP Definition of Done

The MVP is considered complete when:

* the webhook receives a valid visitor event;
* visitor data is normalized;
* the AI produces a structured decision;
* the decision is parsed successfully;
* consent controls prevent unauthorized marketing activation;
* purchase status prevents inappropriate recovery;
* on-site recommendations can be returned to the front end;
* the email demonstration path works when conditions are satisfied;
* synthetic evaluation scenarios are available;
* the workflow is documented and reproducible.

The MVP intentionally prioritizes one reliable end-to-end capability over a larger but unvalidated feature set.
