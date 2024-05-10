def evaluate(env, device, context):
    """
    Evaluate the attributes of Geolocation based on environment, device, and context.

    Args:
    - env (dict): Environment data (e.g., location type).
    - device (dict): Device data.
    - context (dict): Context data.

    Returns:
    - dict: Attributes of the Geolocation factor.
    """
    location_type = env.get('location', 'unknown')
    security = 7 if location_type == 'office' else 5
    intrusiveness = 3
    privacy = 5
    return {
        'Security': security,
        'Intrusiveness': intrusiveness,
        'Privacy': privacy,
        'Accuracy': 2
    }
