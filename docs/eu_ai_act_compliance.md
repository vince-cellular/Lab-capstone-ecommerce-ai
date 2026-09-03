# EU AI Act Compliance Assessment — AI E-commerce Visitor Recovery

## 1. System Overview

The POC is an AI-assisted e-commerce visitor analysis, shopping assistance and customer-recovery workflow.

The system receives behavioural session information such as:

* pages viewed;
* product views;
* time spent on product pages;
* cart activity;
* checkout activity;
* purchase status;
* identification status;
* marketing consent;
* email availability.

An LLM analyses this information and produces a structured recommendation containing:

* recovery risk;
* main behavioural signal;
* recommended action;
* customer message;
* recommended communication channel.

The recommendation is then processed by an n8n workflow that can provide on-site assistance or, where permitted, prepare or trigger an email.

The AI Shopping Assistant can also answer product questions and provide catalogue-grounded product recommendations.

---

## 2. Intended Purpose

The intended purpose is to help an e-commerce business identify customer-journey opportunities, provide relevant shopping assistance and recommend an appropriate next action to improve conversion and customer experience.

The system is not intended to:

* make decisions about employment, credit, insurance, healthcare or access to essential services;
* determine a person's legal status or eligibility;
* make decisions based on sensitive personal characteristics;
* perform biometric identification or biometric categorisation;
* perform emotion recognition;
* autonomously make legally or similarly significant decisions about individuals.

The system is designed primarily for commercial customer assistance, behavioural analysis and marketing/conversion decision support.

The intended purpose is therefore a critical part of the risk classification and must be reassessed if the system is later expanded into a different domain or decision-making context.

---

# 3. EU AI Act Risk Classification

## 3.1 Classification conclusion

Based on the current intended purpose and MVP scope, the system is assessed as **not a high-risk AI system under the EU AI Act**.

This assessment is preliminary and applies only to the described e-commerce marketing, customer-assistance and conversion-optimization use case.

The conclusion must be reassessed if the intended purpose, data processed, level of autonomy or decision-making role changes.

---

## 3.2 Prohibited AI practices assessment

The current system is not designed to perform the prohibited AI practices identified by the EU AI Act.

In particular, the MVP does not use:

* social scoring;
* biometric identification;
* biometric categorisation based on sensitive characteristics;
* emotion recognition;
* manipulative techniques intended to cause serious harm;
* exploitation of vulnerabilities in order to cause serious harm.

The system is specifically designed to avoid sensitive personal characteristics and biometric processing.

Therefore, based on the current intended purpose and functionality, no prohibited AI practice has been identified.

---

## 3.3 High-risk assessment

The EU AI Act identifies specific high-risk AI systems, including systems used in areas such as employment, education, access to essential services, law enforcement, migration and justice.

The present system is an e-commerce customer-assistance and conversion-optimization application.

It is not intended to:

* recruit or evaluate employees;
* assess access to education;
* determine access to healthcare or essential public/private services;
* perform law-enforcement activities;
* make migration or asylum decisions;
* assist courts or judicial authorities.

The system therefore does not currently correspond to the high-risk use cases relevant to its intended purpose.

The system also does not make decisions producing legal or similarly significant effects on individuals.

The AI primarily produces a recommendation such as:

```text
Behavioural evidence
        ↓
Funnel-stage detection
        ↓
Intent assessment
        ↓
Next-best-action recommendation
        ↓
Consent / eligibility controls
        ↓
Human or workflow action
```

The AI recommendation is therefore a decision-support output rather than an autonomous high-impact decision.

### Important limitation

This classification is dependent on the current intended purpose.

If the system were later used for decisions involving employment, credit, insurance, healthcare, essential services or other regulated/high-impact domains, a new EU AI Act classification would be required.

---

# 4. Transparency Obligations

The AI Shopping Assistant directly interacts with website visitors.

Article 50 of the EU AI Act requires applicable AI systems intended to interact directly with natural persons to ensure that people are informed that they are interacting with an AI system, unless this is already obvious from the circumstances.

The European Commission states that these transparency obligations apply from **2 August 2026**.

The MVP will therefore clearly disclose the AI nature of the assistant.

Example:

> **"You are interacting with an AI shopping assistant."**

This disclosure should be visible at the beginning of the interaction and remain sufficiently clear to the visitor.

The system should also avoid presenting AI-generated communications in a way that intentionally deceives customers about their origin.

Article 50 also contains separate requirements concerning marking or labelling certain AI-generated content. The exact obligation depends on the type of output and the role of the organisation in the AI supply chain.

---

# 5. Human Oversight

The current POC limits the AI primarily to analysis and recommendation.

The AI does not independently determine:

* discounts;
* prices;
* refunds;
* credit;
* access to essential services;
* employment decisions;
* other legally or similarly significant decisions.

For production deployment, human oversight and escalation should remain available for:

* unusual or ambiguous cases;
* complaints;
* sensitive customer situations;
* disputed transactions;
* unexpected AI recommendations;
* recommendations that may create customer, financial or compliance risk.

For outbound marketing, the recommended architecture is:

```text
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
```

This separation prevents the LLM from independently deciding whether a customer may legally be contacted.

---

# 6. Accuracy, Robustness and Monitoring

The POC includes an evaluation process using LangSmith.

The evaluation process considers:

* correctness;
* answer relevance;
* hallucination;
* bias and fairness.

The evaluation results are treated as development evidence rather than production performance guarantees.

The initial evaluation also identified an integration/mapping limitation. Results affected by this limitation are therefore not presented as evidence of production-level performance.

Production deployment should continuously monitor:

* incorrect recommendations;
* hallucinations;
* latency;
* token consumption;
* failed workflow executions;
* inappropriate communication decisions;
* customer complaints;
* opt-outs;
* intervention frequency.

The system should also maintain a fallback behaviour so that the e-commerce website remains functional if the AI service becomes unavailable.

---

# 7. Technical Documentation

Before production deployment, the organisation should maintain documentation covering:

* system purpose and intended use;
* system architecture;
* input and output data;
* model/provider information;
* prompts and decision logic;
* evaluation methodology;
* monitoring methodology;
* known limitations;
* human oversight mechanisms;
* security controls;
* data-protection measures;
* incident-management procedures;
* change-management procedures.

Where applicable, documentation should distinguish between responsibilities of the application provider/deployer and responsibilities of the underlying AI model provider.

---

# 8. Key Existing Controls

The POC already includes several safeguards in the AI system prompt and workflow.

These include:

* marketing email is not recommended when marketing consent is false;
* cart recovery is not recommended after a purchase;
* the AI is instructed not to invent products, prices, promotions, availability or customer information;
* the AI must use only the behavioural evidence provided;
* unavailable information must be identified as unknown;
* the AI must return structured JSON for downstream automation;
* anonymous visitors are not individually identified;
* sensitive personal characteristics are outside the MVP scope.

These controls reduce the risk of unsupported recommendations and inappropriate automated actions.

---

# 9. GDPR Relationship

EU AI Act compliance does not replace GDPR compliance.

The system may process behavioural and potentially personal information, particularly when visitors are identified or an email address is available.

Therefore, the GDPR assessment is documented separately in:

`docs/gdpr_documentation.md`

The production organisation must assess:

* lawful bases;
* purpose limitation;
* data minimisation;
* retention;
* data-subject rights;
* profiling;
* automated decision-making;
* third-party processing;
* international transfers;
* security;
* DPIA requirements.

The AI Act classification and GDPR assessment should therefore be treated as related but separate compliance workstreams.

---

# 10. Production Compliance Gaps

Before production deployment, the following should be completed:

1. Formal legal review of the AI Act classification.
2. Confirmation of the exact provider/deployer roles.
3. Detailed technical documentation.
4. AI provider and third-party contractual review.
5. Formal GDPR/data-protection assessment.
6. DPIA screening and DPIA where required.
7. Human oversight and escalation procedures.
8. Monitoring and incident-management procedures.
9. Documentation of model changes and evaluations.
10. Customer-facing transparency information.
11. Security and access-control validation.
12. Data-retention and deletion procedures.

---

# 11. Compliance Status

| Area                     | Current POC status                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| Prohibited AI practices  | No prohibited practice identified                                                            |
| High-risk classification | Preliminary assessment: not high-risk                                                        |
| AI transparency          | Required for applicable direct AI interaction; implemented/planned for AI Shopping Assistant |
| Human oversight          | Decision-support architecture                                                                |
| Sensitive profiling      | Out of scope                                                                                 |
| Biometric processing     | Out of scope                                                                                 |
| GDPR                     | Addressed separately; production assessment required                                         |
| DPIA                     | Production DPIA screening required                                                           |
| Production conformity    | Not claimed at POC stage                                                                     |

---

# 12. Conclusion

The current POC represents a relatively limited-risk e-commerce AI use case.

Based on its current intended purpose, it does not appear to fall within the EU AI Act's prohibited or high-risk use cases.

The main AI Act requirement directly relevant to the customer-facing AI Shopping Assistant is transparency: visitors should be informed that they are interacting with an AI system. Article 50 transparency requirements apply from 2 August 2026.

The system also incorporates human oversight, scope restrictions, structured outputs and safeguards against unsupported recommendations.

However, the POC should **not** be presented as proof of full legal compliance.

Before production deployment, the organisation must validate the classification, complete the relevant GDPR and data-protection work, verify third-party arrangements, implement production security and monitoring controls, and reassess the classification if the intended purpose or functionality changes.

The recommended next step is therefore a controlled pilot followed by a formal production-readiness and compliance review.
