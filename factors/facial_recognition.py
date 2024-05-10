def evaluate(env, device, context):
    """
    Evaluate the attributes of Facial Recognition based on environment, device, and context.

    Args:
    - env (dict): Environment data.
    - device (dict): Device data (e.g., camera quality).
    - context (dict): Context data (e.g., user consent).

    Returns:
    - dict: Attributes of the Facial Recognition modality.
    """
    security = 9 if device.get('camera') == 'HD' else 6
    intrusiveness = 3
    privacy = 8 if context.get('consent') else 4
    return {
        'Security': security,
        'Intrusiveness': intrusiveness,
        'Privacy': privacy,
        'Accuracy': 4
    }
