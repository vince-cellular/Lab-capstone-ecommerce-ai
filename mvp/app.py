import json
from pathlib import Path

import streamlit as st

from src.behavior_analyzer import analyze_behavior
from src.recommendation_engine import generate_recommendation
from src.product_assistant import get_product_assistance_message
from src.llm_analyzer import analyze_with_llm


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI E-commerce Conversion Advisor",
    page_icon="🛍️",
    layout="wide"
)


# --------------------------------------------------
# Load visitor data
# --------------------------------------------------

DATA_PATH = Path(__file__).parent / "data" / "sample_visitors.json"


def load_visitors():
    """Load synthetic visitor data from the JSON file."""
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# --------------------------------------------------
# Application title
# --------------------------------------------------

st.title("🛍️ AI E-commerce Conversion & Shopping Advisor")

st.write(
    "Analyze visitor behavior, identify conversion opportunities, "
    "and recommend the next best action."
)


# --------------------------------------------------
# Visitor selector
# --------------------------------------------------

visitors = load_visitors()

visitor_options = {
    visitor["visitor_id"]: visitor
    for visitor in visitors
}

selected_visitor_id = st.selectbox(
    "Select a visitor scenario",
    options=list(visitor_options.keys())
)

selected_visitor = visitor_options[selected_visitor_id]


# --------------------------------------------------
# Visitor behavior
# --------------------------------------------------

st.subheader("Visitor Behavior")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Pages Viewed",
        selected_visitor.get("pages_viewed", 0)
    )

    st.metric(
        "Product Views",
        selected_visitor.get("product_views", 0)
    )

    st.metric(
        "Product Engagement",
        f"{selected_visitor.get('time_on_product_seconds', 0)} sec"
    )


with col2:
    st.metric(
        "Added to Cart",
        "Yes" if selected_visitor.get("added_to_cart") else "No"
    )

    st.metric(
        "Checkout Started",
        "Yes" if selected_visitor.get("checkout_started") else "No"
    )

    st.metric(
        "Purchased",
        "Yes" if selected_visitor.get("purchased") else "No"
    )


with col3:
    st.metric(
        "Returning Visitor",
        "Yes" if selected_visitor.get("returning_visitor") else "No"
    )

    st.metric(
        "Product Questions",
        selected_visitor.get("product_questions", 0)
    )

    st.metric(
        "Marketing Consent",
        "Yes" if selected_visitor.get("consent_marketing") else "No"
    )


# --------------------------------------------------
# AI Behavioral Analysis
# --------------------------------------------------

st.divider()

st.subheader("AI Behavioral Analysis")

if st.button("🔍 Analyze Behavior", type="primary"):

    analysis = analyze_behavior(selected_visitor)

    st.session_state["analysis"] = analysis

    recommendation = generate_recommendation(
        selected_visitor,
        analysis
    )

    st.session_state["recommendation"] = recommendation

    try:
        with st.spinner("AI is interpreting visitor behavior..."):

            llm_analysis = analyze_with_llm(
                selected_visitor,
                analysis
            )

            st.session_state["llm_analysis"] = llm_analysis

        st.success("Behavior and AI analysis completed.")

    except Exception as error:

        st.session_state.pop("llm_analysis", None)

        st.warning(
            "The deterministic analysis completed successfully, "
            "but the LLM analysis could not be generated."
        )

        st.error(str(error))

# --------------------------------------------------
# Display behavioral analysis
# --------------------------------------------------

if "analysis" in st.session_state:

    analysis = st.session_state["analysis"]

    st.subheader("Behavioral Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Purchase Intent Score",
            f"{analysis['behavioral_score']}/100"
        )

    with col2:
        st.metric(
            "Funnel Stage",
            analysis["funnel_stage"].replace("_", " ").title()
        )

    with col3:
        st.metric(
            "Behavioral Segment",
            analysis["segment"].replace("_", " ").title()
        )

    st.write("**Reason:**")

    st.info(analysis["reason"])

# --------------------------------------------------
# LLM Business Interpretation
# --------------------------------------------------

if "llm_analysis" in st.session_state:

    llm_analysis = st.session_state["llm_analysis"]

    st.divider()

    st.subheader("🧠 AI Business Interpretation")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Purchase Intent Interpretation**")
        st.info(
            llm_analysis["purchase_intent_interpretation"]
        )

        st.write("**Customer Need**")
        st.write(
            llm_analysis["customer_need"]
        )

    with col2:
        st.write("**Conversion Risk**")
        st.warning(
            llm_analysis["conversion_risk"]
        )

        st.write("**AI Recommended Intervention**")
        st.success(
            llm_analysis["recommended_intervention"]
        )

    st.write("**AI Explanation**")
    st.write(
        llm_analysis["explanation"]
    )

# --------------------------------------------------
# Recommended Next Action
# --------------------------------------------------

if "recommendation" in st.session_state:

    recommendation = st.session_state["recommendation"]

    st.divider()

    st.subheader("🎯 Recommended Next Action")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Channel**")

        st.info(
            recommendation["channel"].replace("_", " ").title()
        )

    with col2:
        st.write("**Recommended Action**")

        st.success(
            recommendation["action"].replace("_", " ").title()
        )

    st.write("**Reason:**")

    st.write(recommendation["reason"])


# --------------------------------------------------
# Consent & Activation Check
# --------------------------------------------------

    st.divider()

    st.subheader("🔐 Consent & Activation Check")

    if not selected_visitor.get("identified", False):

        st.warning(
            "Anonymous visitor: no identity-based outbound marketing "
            "action is permitted."
        )

        st.write(
            "**Allowed intervention:** "
            "On-site assistance / AI Shopping Assistant"
        )

    elif not selected_visitor.get("consent_marketing", False):

        st.warning(
            "Marketing consent is not available. Outbound marketing "
            "activation is blocked."
        )

        st.write(
            "**Allowed intervention:** On-site assistance only"
        )

    else:

        st.success(
            "Marketing consent is available. The recommended outbound "
            "action may proceed to human approval."
        )

        st.write(
            "**Next step:** Human approval before activation"
        )


# --------------------------------------------------
# AI Shopping Assistant
# --------------------------------------------------

st.divider()

st.subheader("🤖 AI Shopping Assistant")

if "analysis" in st.session_state:

    analysis = st.session_state["analysis"]

    if analysis["segment"] == "product_uncertainty":

        st.write(
            "The visitor appears to need help choosing between products."
        )

        if st.button("💬 Offer Product Assistance"):

            message = get_product_assistance_message(analysis)

            st.info(message)

    elif not selected_visitor.get("identified", False):

        st.write(
            "The visitor is anonymous. The assistant can provide "
            "on-site shopping assistance without identifying the visitor."
        )

        if st.button("💬 Open AI Shopping Assistant"):

            message = get_product_assistance_message(analysis)

            st.info(message)

    else:

        st.write(
            "The shopping assistant is available for "
            "on-site customer assistance."
        )