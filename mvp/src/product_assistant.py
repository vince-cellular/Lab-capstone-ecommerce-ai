def get_product_assistance_message(analysis):
    """
    Generate a simple shopping-assistance message
    based on the visitor's behavioral analysis.

    This is the baseline version.
    The real LLM-powered assistant will be added later.
    """

    segment = analysis.get("segment")

    if segment == "product_uncertainty":
        return (
            "It looks like you may be comparing several products. "
            "I can help you compare their features and find the option "
            "that best matches your needs."
        )

    if segment in ["high_intent", "high_intent_returning"]:
        return (
            "I can help you find the right product and answer any "
            "questions before you make your purchase."
        )

    if segment == "cart_abandonment":
        return (
            "Need help completing your purchase? "
            "I can answer questions about the products in your cart."
        )

    if segment == "checkout_abandonment":
        return (
            "Need help completing your order? "
            "I can help answer product or purchase-related questions."
        )

    return (
        "Hi! I'm your AI shopping assistant. "
        "I can help you find products and answer questions."
    )