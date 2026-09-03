# GDPR Documentation — AI E-commerce Conversion & Shopping Advisor

## 1. Purpose

This document assesses the main GDPR and privacy considerations for the **AI E-commerce Conversion & Shopping Advisor**.

The solution analyses permitted customer-journey signals to identify potential conversion opportunities and recommend appropriate next actions.

The POC is designed according to privacy-by-design principles and uses synthetic or public data only. It is not presented as proof of production GDPR compliance.

---

## 2. Scope and Intended Processing

The system processes behavioural and contextual information to:

* understand customer-journey behaviour;
* detect potential purchase intent;
* identify funnel stages such as product consideration, cart abandonment or checkout abandonment;
* provide relevant on-site AI assistance;
* recommend appropriate recovery actions;
* support permitted customer-recovery activities;
* measure the effectiveness of the workflow.

The system must not use the data for unrelated purposes without an appropriate legal basis and appropriate transparency.

---

## 3. Anonymous and Identified Visitors

A central privacy control is the separation between **anonymous visitors** and **identified visitors**.

### Anonymous visitors

The system may analyse permitted session-level behavioural signals such as:

* products viewed;
* number of product views;
* time spent on relevant pages;
* returning-visitor status;
* cart activity;
* checkout activity.

The system does **not** attempt to discover or infer the identity of an anonymous visitor.

Anonymous behavioural information may be used to:

* provide on-site AI assistance;
* generate anonymous behavioural segments;
* analyse aggregate customer-journey patterns;
* identify conversion opportunities.

An anonymous visitor is not individually contacted by email or SMS.

### Identified visitors

Where a visitor is legitimately identified through an existing customer relationship, account or other permitted mechanism, the workflow may process relevant customer and behavioural information.

Outbound communication remains subject to applicable legal requirements, consent and eligibility checks.

---

## 4. Data Processed

Depending on the scenario, the POC may process:

* visitor identifier;
* identification status;
* marketing consent status;
* returning-visitor status;
* pages viewed;
* product views;
* product/category interactions;
* time spent on relevant pages;
* cart activity;
* checkout activity;
* purchase status;
* product questions;
* email address when legitimately available;
* AI interaction information.

The system should avoid collecting or processing unnecessary sensitive personal data.

The POC does not intentionally process special-category data such as health information, religion, political opinions, ethnicity or sexual orientation.

---

## 5. Data Flow

The simplified architecture is:

```text
Customer interaction
        ↓
E-commerce website
        ↓
Visitor event
        ↓
n8n webhook
        ↓
Data preparation
        ↓
Behaviour analysis
        ↓
Funnel / segment / intent assessment
        ↓
Next-best-action recommendation
        ↓
Consent / eligibility check
        ↓
On-site AI assistance
        OR
Approved activation recommendation
```

For production deployment, each processing activity and data transfer must be documented.

---

## 6. Purpose Limitation

Personal and behavioural information should only be processed for clearly defined purposes related to the stated e-commerce use case.

Permitted purposes may include:

* customer assistance;
* conversion analysis;
* recovery of abandoned carts or checkouts where legally permitted;
* recommendation of relevant products;
* customer-journey optimisation;
* measurement and evaluation of the AI workflow.

The data should not subsequently be reused for unrelated profiling, advertising or other purposes without an appropriate legal basis and transparency.

---

## 7. Lawful Basis

The production organisation must determine the appropriate GDPR lawful basis for each processing activity.

Depending on the specific implementation, potential bases may include:

* consent;
* performance of a contract;
* legitimate interests, where applicable and supported by an appropriate balancing assessment.

The POC does not assume that the presence of an email address automatically provides permission for marketing communication.

The legal basis must be assessed separately for:

1. behavioural analytics;
2. on-site assistance;
3. customer communications;
4. marketing communications;
5. profiling or segmentation;
6. AI processing.

---

## 8. Marketing Consent

Marketing consent is explicitly represented in the visitor data.

The workflow contains a safeguard preventing marketing activation when the required consent is absent.

The AI decision logic also follows the rule:

> If marketing consent is false, do not recommend marketing email or marketing messaging.

The architecture is therefore:

```text
AI recommendation
        ↓
Consent / eligibility check
        ↓
      Approved?
      /       \
    YES        NO
     ↓          ↓
Activation   No outbound
             marketing
```

The availability of an email address alone does not automatically authorise marketing communication.

---

## 9. Data Minimisation

The AI should receive only information necessary to perform the specific task.

For example, a product-recovery analysis may use:

```text
Product category: Running shoes
Products viewed: 3
Add to cart: Yes
Checkout started: Yes
Purchase: No
Intent score: 91
```

It does not normally require:

* full postal address;
* payment-card information;
* unrelated customer information;
* unnecessary demographic information.

Where an AI provider is used, unnecessary personal information should be removed before the information is sent to the model.

---

## 10. AI Shopping Assistant

The AI Shopping Assistant is designed to help visitors make product decisions.

It may:

* answer product questions;
* compare products;
* explain product differences;
* ask about customer requirements;
* recommend products from an approved catalogue.

The assistant must not invent:

* products;
* prices;
* specifications;
* availability;
* promotions;
* customer information.

The assistant should be clearly identified as an AI system.

---

## 11. Profiling and Automated Decision-Making

The system analyses behavioural signals to identify purchase intent, funnel stage and potential recovery opportunities.

This may constitute profiling depending on the production implementation and must therefore be assessed by the organisation before deployment.

The POC is designed as a **decision-support system**.

It does not make decisions producing legal or similarly significant effects on individuals.

The AI does not independently determine:

* credit eligibility;
* insurance eligibility;
* employment decisions;
* healthcare decisions;
* access to essential services;
* legal status.

If the production implementation becomes substantially more autonomous or its decisions become legally or similarly significant, a new GDPR assessment must be performed.

---

## 12. Data Retention

The production organisation should establish documented retention periods for:

* visitor events;
* behavioural data;
* AI inputs;
* AI outputs;
* workflow logs;
* contact information;
* marketing-consent records;
* evaluation datasets.

Data should not be retained indefinitely.

Retention periods should be implemented technically through deletion, anonymisation or aggregation mechanisms where appropriate.

---

## 13. Data Subject Rights

The production implementation must support applicable GDPR rights, including:

* right of access;
* right to rectification;
* right to erasure;
* right to restriction of processing;
* right to data portability where applicable;
* right to object where applicable;
* applicable rights concerning automated decision-making and profiling.

The production system should provide a process for locating, correcting or deleting relevant personal information.

---

## 14. DPIA Assessment

A Data Protection Impact Assessment should be formally considered before production deployment.

The current POC:

* uses synthetic/public data;
* does not intentionally process special-category data;
* does not attempt to identify anonymous visitors;
* does not perform biometric processing;
* does not make legally or similarly significant decisions.

However, a production DPIA assessment should consider:

* scale of behavioural monitoring;
* systematic profiling;
* number of individuals affected;
* types of behavioural data processed;
* combination of datasets;
* degree of automation;
* third-party processing;
* international transfers;
* potential impact on individuals.

If the production processing is likely to result in a high risk to individuals, the required DPIA should be completed before processing begins.

---

## 15. Third-Party Processors

The production architecture may involve:

* n8n or other automation infrastructure;
* LLM/API providers;
* e-commerce platforms;
* email providers;
* monitoring and evaluation platforms;
* analytics services.

The production organisation must identify the role of each provider and establish appropriate contractual and data-protection safeguards.

Where applicable, Data Processing Agreements should be established and reviewed.

---

## 16. International Data Transfers

Where personal data is transferred outside the European Economic Area, the organisation must verify the applicable GDPR transfer mechanism and safeguards.

The production documentation should identify:

* where data is stored;
* where processing occurs;
* which providers receive personal data;
* applicable transfer mechanisms;
* contractual safeguards;
* relevant technical safeguards.

---

## 17. Security

Production deployment should implement appropriate technical and organisational measures, including:

* encryption in transit;
* secure authentication;
* access controls;
* least-privilege permissions;
* secure API credentials;
* logging;
* monitoring;
* incident response;
* secure retention;
* secure deletion;
* appropriate backup controls.

API keys, passwords and other credentials must never be stored directly in source code or public repositories.

---

## 18. Privacy-by-Design Controls

The POC incorporates several privacy-oriented controls:

1. Separation of anonymous and identified visitors.
2. No attempt to identify anonymous visitors.
3. No individual outbound marketing for anonymous visitors.
4. Explicit marketing-consent handling.
5. Data minimisation before AI processing.
6. Avoidance of sensitive personal characteristics.
7. No biometric identification or categorisation.
8. No autonomous legally significant decision-making.
9. AI recommendations are separated from consent/eligibility checks.
10. Product recommendations are grounded in an approved catalogue.
11. Synthetic/public data is used for the demonstration.

---

## 19. Production Compliance Gaps

Before production deployment, the organisation should confirm:

1. Controller and processor roles.
2. Lawful basis for each processing activity.
3. Privacy notice and transparency requirements.
4. Marketing consent requirements.
5. Retention periods.
6. Data-subject request procedures.
7. Profiling assessment.
8. DPIA requirement.
9. Third-party processor agreements.
10. International transfer safeguards.
11. Security controls.
12. AI provider contractual arrangements.
13. Incident-management procedures.
14. Data deletion and anonymisation mechanisms.

---

## 20. POC Limitations

This document is a preliminary privacy assessment for an educational/business POC.

It does not constitute:

* a formal legal opinion;
* a completed DPIA;
* a declaration of GDPR compliance;
* legal advice for a specific production organisation.

The production company remains responsible for determining the applicable legal requirements based on its actual processing activities, jurisdictions, technologies and contractual relationships.

---

## 21. Conclusion

The AI E-commerce Conversion & Shopping Advisor incorporates privacy-by-design principles by separating anonymous and identified visitors, limiting the use of personal data, enforcing marketing-consent controls and preventing unnecessary identity-based outbound communication.

The POC does not attempt to identify anonymous visitors and does not intentionally process sensitive personal characteristics.

The AI acts primarily as a decision-support and customer-assistance system rather than an autonomous system making legally or similarly significant decisions.

The POC should therefore **not be presented as fully GDPR compliant**.

Before production deployment, the organisation must complete the appropriate legal, data-protection, security, contractual and governance assessments, including a formal determination of the applicable lawful bases and whether a DPIA is required.
