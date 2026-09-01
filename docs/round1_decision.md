# Round 1 Decision — AI E-commerce Customer Recovery

## 1. Executive Summary

The Round 1 project evaluated the feasibility of using AI to identify potentially recoverable e-commerce sessions and generate personalized customer-recovery recommendations.

The solution combines:

* **Tableau** for business and dataset analysis
* **n8n** for workflow automation
* **an LLM** for behavioral analysis and recommendation generation
* **LangSmith** for AI evaluation and monitoring

The initial POC demonstrates that the technical approach is feasible.

## 2. Business Opportunity

E-commerce companies generate a large number of visitor sessions that do not result in revenue.

AI could potentially help identify high-value or high-risk sessions and recommend appropriate recovery actions, such as:

* personalized follow-up
* product recommendations
* customer assistance
* retargeting
* recovery messaging

The objective is not to automate every customer interaction, but to identify situations where AI-assisted intervention could create measurable business value.

## 3. Data Analysis — Tableau

The available e-commerce dataset was analyzed using **Tableau** to identify behavioral patterns and potential opportunities for AI-assisted customer recovery.

The dashboard provides stakeholder-oriented metrics and visualizations that help identify:

* visitor behavior
* conversion/revenue patterns
* traffic-type differences
* session characteristics
* potential high-value non-converting sessions

These insights were used to inform the design of the AI use case and the test scenarios used in the POC.

## 4. Evidence from the POC

The n8n workflow successfully processes structured visitor information and generates an AI recommendation.

The current workflow is:

**Manual Trigger → Edit Fields → Message a Model**

Example test case:

* Visitor type: Returning
* Product pages viewed: 25
* Session duration: 90 seconds
* Traffic type: 13
* Revenue: False
* Estimated cart value: €149.99

The AI classified the recovery risk as **High** and generated both a recommended action and a customer-facing message.

The model also recognized information limitations, including the unknown meaning of traffic type 13 and the absence of explicit cart-abandonment information.

## 5. Evaluation Evidence

The AI workflow was tested through **LangSmith**.

The evaluation environment provides evidence for:

* multiple experiments
* five test cases per experiment
* latency measurement
* token usage
* correctness evaluation
* hallucination/groundedness evaluation

The initial results demonstrate that AI quality can be monitored systematically rather than evaluated only through subjective inspection.

However, the initial correctness result requires further investigation before the evaluation can be considered conclusive.

## 6. Key Findings

### Positive findings

* The AI workflow is technically feasible.
* The workflow successfully executes from structured input to AI output.
* The model can identify behavioral signals from the available data.
* The model can produce actionable recommendations.
* The model can generate customer-facing communication.
* Token usage and latency can be monitored.
* LangSmith provides a framework for systematic AI evaluation.
* Tableau provides a business-facing view of the underlying e-commerce data.

### Limitations

* The POC uses manually created test data.
* The dataset does not contain all business variables required for a production decision.
* Traffic-type codes are not semantically defined.
* Cart abandonment is not explicitly provided.
* The evaluation dataset is currently small.
* The correctness evaluator requires validation.
* No real-world recovery conversion has yet been measured.

## 7. Risk Assessment

### AI quality risk

The model may generate an incorrect or poorly justified recommendation.

**Mitigation:** expand the evaluation dataset and establish validated reference answers.

### Hallucination / grounding risk

The model could infer information that is not present in the input.

**Mitigation:** require the model to distinguish known facts from assumptions and monitor groundedness.

### Business risk

A recommendation may not lead to an actual increase in revenue.

**Mitigation:** validate the solution through a controlled pilot and measure recovery conversion.

### Data protection risk

A production implementation may process customer-related information.

**Mitigation:** conduct an appropriate GDPR/data-protection assessment before production deployment.

## 8. Cost and Timeline

### Estimated upfront implementation

Approximately **€4,500** for a small/medium-business POC-to-initial implementation, subject to technical discovery.

### Estimated monthly operating cost

Approximately **€90–€400/month**, depending on AI usage, infrastructure, monitoring and communication volume.

### Indicative timeline

* POC: **1–2 weeks**
* Pilot: **3–4 weeks**
* Production deployment: **approximately 6–8 weeks total**

These are preliminary estimates and depend on integration complexity, data availability and business requirements.

## 9. Round 1 Recommendation

### CONDITIONAL GO

The project should proceed to the next phase, but not directly to full production deployment.

The POC has demonstrated sufficient technical feasibility to justify a controlled pilot.

Before moving to production, the following conditions should be satisfied:

1. Validate the correctness evaluation methodology.
2. Expand the evaluation dataset.
3. Compare multiple AI models.
4. Establish business-specific quality thresholds.
5. Test hallucination/groundedness systematically.
6. Connect the workflow to realistic e-commerce data.
7. Measure actual recovery/conversion performance.
8. Validate GDPR and data-protection requirements.
9. Confirm the economic value against implementation and operating costs.

## 10. Success Criteria for the Next Phase

The pilot should be considered successful if it demonstrates:

* acceptable AI correctness
* low hallucination/grounding risk
* acceptable response latency
* predictable AI operating cost
* measurable business improvement
* safe and appropriate customer communication

The final production decision should be based on these measurable criteria rather than technical feasibility alone.

## 11. Final Conclusion

Round 1 demonstrates that an AI-assisted e-commerce recovery solution is technically feasible and potentially valuable.

**Tableau** provides the business analysis layer, **n8n** demonstrates the automation workflow, and **LangSmith** provides the AI evaluation and monitoring layer.

The current evidence is sufficient to justify moving forward with a controlled pilot, but not sufficient to justify unrestricted production deployment.

**Decision: CONDITIONAL GO — proceed to pilot validation after improving AI evaluation and connecting the POC to more realistic business data.**
