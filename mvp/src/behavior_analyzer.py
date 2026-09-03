def analyze_behavior(visitor):
    """
    Analyze a visitor's behavior and determine:
    - behavioral score
    - funnel stage
    - behavioral segment
    - reason
    """

    score = 0
    signals = []

    # Purchase intent signals
    if visitor.get("product_views", 0) >= 3:
        score += 20
        signals.append("multiple product views")

    if visitor.get("time_on_product_seconds", 0) >= 180:
        score += 20
        signals.append("high product engagement")

    if visitor.get("added_to_cart"):
        score += 25
        signals.append("added product to cart")

    if visitor.get("checkout_started"):
        score += 25
        signals.append("started checkout")

    if visitor.get("returning_visitor"):
        score += 10
        signals.append("returning visitor")

    if visitor.get("product_questions", 0) >= 2:
        score += 15
        signals.append("multiple product questions")

    # Determine funnel stage
    if visitor.get("purchased"):
        funnel_stage = "purchased"

    elif visitor.get("checkout_started"):
        funnel_stage = "checkout"

    elif visitor.get("added_to_cart"):
        funnel_stage = "cart"

    elif visitor.get("product_views", 0) > 0:
        funnel_stage = "product_consideration"

    else:
        funnel_stage = "discovery"

    # Determine behavioral segment
    if visitor.get("purchased"):
        segment = "customer"

    elif visitor.get("checkout_started"):
        segment = "checkout_abandonment"

    elif visitor.get("added_to_cart"):
        segment = "cart_abandonment"

    elif visitor.get("product_questions", 0) >= 2:
        segment = "product_uncertainty"

    elif visitor.get("returning_visitor") and score >= 30:
        segment = "high_intent_returning"

    elif score >= 50:
        segment = "high_intent"

    else:
        segment = "low_or_medium_intent"

    # Build explanation
    reason = ", ".join(signals)

    return {
        "visitor_id": visitor.get("visitor_id"),
        "identified": visitor.get("identified", False),
        "marketing_consent": visitor.get("consent_marketing", False),
        "behavioral_score": min(score, 100),
        "funnel_stage": funnel_stage,
        "segment": segment,
        "reason": reason
    }