import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def analyze_with_llm(visitor, deterministic_analysis):
    """
    Use an LLM to provide contextual analysis of visitor behavior.

    The deterministic analysis is provided to the LLM as structured context.
    The LLM does not make consent or legal decisions.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not configured. "
            "Please add it to the .env file."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an AI e-commerce conversion advisor.

Analyze the following synthetic visitor behavior.

Visitor data:
{json.dumps(visitor, indent=2)}

Deterministic behavioral analysis:
{json.dumps(deterministic_analysis, indent=2)}

Your task is to provide a concise business interpretation.

Return ONLY valid JSON with these fields:

{{
  "purchase_intent_interpretation": "...",
  "customer_need": "...",
  "conversion_risk": "...",
  "recommended_intervention": "...",
  "explanation": "..."
}}

Important rules:

1. Use only the information provided.
2. Do not infer sensitive personal characteristics.
3. Do not attempt to identify an anonymous visitor.
4. Do not make legal or consent decisions.
5. Do not invent products, prices or customer information.
6. Treat the deterministic analysis as an input signal, not as absolute truth.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return json.loads(response.output_text)