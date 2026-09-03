def generate_recommendation(visitor, analysis):
    """
    Generate a recommended intervention based on:
    - visitor identity status
    - marketing consent
    - behavioral segment

    The function recommends an action.
    It does not execute or send the action.
    """

    segment = analysis["segment"]
    identified = analysis["identified"]
    consent = analysis["marketing_consent"]

    # ---------------------------------------------------------
    # 1. ANONYMOUS VISITOR
    # ---------------------------------------------------------
    if not identified:

        if segment in ["high_intent", "high_intent_returning"]:
            return {
                "channel": "onsite_popup",
                "action": "open_ai_shopping_assistant",
                "reason": "High purchase intent detected.",
                "requires_marketing_consent": False
            }

        if segment == "product_uncertainty":
            return {
                "channel": "onsite_popup",
                "action": "offer_product_assistance",
                "reason": "Visitor appears uncertain about product selection.",
                "requires_marketing_consent": False
            }

        return {
            "channel": "onsite",
            "action": "continue_personalized_experience",
            "reason": "No strong intervention signal detected.",
            "requires_marketing_consent": False
        }

    # ---------------------------------------------------------
    # 2. IDENTIFIED VISITOR + MARKETING CONSENT
    # ---------------------------------------------------------
    if identified and consent:

        if segment == "cart_abandonment":
            return {
                "channel": "email",
                "action": "recommend_cart_recovery",
                "reason": "Identified visitor abandoned cart.",
                "requires_marketing_consent": True
            }

        if segment == "checkout_abandonment":
            return {
                "channel": "email",
                "action": "recommend_checkout_recovery",
                "reason": "Identified visitor started checkout but did not purchase.",
                "requires_marketing_consent": True
            }

        if segment in ["high_intent", "high_intent_returning"]:
            return {
                "channel": "email_or_onsite",
                "action": "recommend_personalized_follow_up",
                "reason": "High-intent identified visitor has not purchased.",
                "requires_marketing_consent": True
            }

    # ---------------------------------------------------------
    # 3. IDENTIFIED VISITOR WITHOUT MARKETING CONSENT
    # ---------------------------------------------------------
    if segment == "product_uncertainty":
        return {
            "channel": "onsite_popup",
            "action": "offer_product_assistance",
            "reason": (
                "Visitor appears uncertain about product selection. "
                "Outbound marketing is blocked because marketing consent "
                "is not available."
            ),
            "requires_marketing_consent": False
        }

    return {
        "channel": "onsite",
        "action": "continue_onsite_assistance",
        "reason": (
            "Marketing activation is not permitted without appropriate consent."
        ),
        "requires_marketing_consent": True
    }