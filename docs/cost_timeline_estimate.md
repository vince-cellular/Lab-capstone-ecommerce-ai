# Cost & Timeline Estimate

## 1. POC Architecture

The e-commerce AI recovery POC uses the following architecture:

Website visitor
→ n8n webhook
→ Visitor data processing
→ GPT-5-mini decision engine
→ Structured AI decision
→ Channel routing
→ On-site assistance or email recovery

## 2. Estimated Implementation Timeline

| Component | Estimated Time |
|---|---:|
| Website event tracking | 1 day |
| n8n webhook and data processing | 0.5 day |
| AI decision engine | 1 day |
| Decision parsing and routing | 0.5 day |
| Email integration | 0.5 day |
| Testing and debugging | 1 day |
| Evaluation setup | 0.5 day |
| Documentation | 0.5 day |
| **Total estimated MVP effort** | **5.5 days** |

## 3. Estimated Operating Costs

The main variable operating cost is LLM usage.

For each visitor event requiring an AI decision, the system sends behavioral session data to GPT-5-mini and receives a structured decision.

Other infrastructure costs depend on the production deployment configuration and are therefore excluded from this POC estimate.

### Main cost drivers

- Number of visitor events processed
- Average input tokens per request
- Average output tokens per request
- LLM model selected
- Number of AI decisions generated per visitor/session
- n8n hosting/infrastructure
- Email delivery volume

## 4. Cost Optimization Opportunities

The production system could reduce operating costs by:

1. Triggering the AI only when meaningful behavioral signals are detected.
2. Avoiding repeated AI calls during the same visitor session.
3. Using deterministic rules for simple cases.
4. Reserving the LLM for ambiguous or high-value situations.
5. Limiting the amount of session data sent to the model.
6. Monitoring token usage and latency through LangSmith.

## 5. Business Value

The POC is designed to improve e-commerce conversion by identifying high-intent visitors and selecting an appropriate intervention.

Potential business KPIs include:

- Conversion rate
- Cart recovery rate
- Checkout completion rate
- Revenue per visitor
- Email recovery conversion
- On-site assistance conversion
- AI intervention rate
- Cost per AI intervention
- Incremental revenue generated

## 6. Production Scaling

Before production deployment, the following areas would require further validation:

- Larger-scale evaluation dataset
- Production traffic testing
- LLM cost monitoring
- Latency monitoring
- Consent and privacy compliance validation
- Email deliverability
- Failure handling and fallback logic
- A/B testing against a non-AI control group

## 7. POC Conclusion

The current POC demonstrates the technical feasibility of using behavioral visitor data and an LLM-based decision engine to select personalized e-commerce recovery actions.

The next stage would be a controlled production pilot measuring incremental conversion and revenue impact against a baseline.