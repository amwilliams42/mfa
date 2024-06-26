from mfa import evaluate_and_select_factors


def determine_attribute_constraints(env, device, context):
    """
    Determine dynamic attribute constraints based on environment, device, and context data.

    Args:
    - env (dict): Environment data.
    - device (dict): Device data.
    - context (dict): Context data (e.g., security rating of request, last login time).

    Returns:
    - dict: Attribute constraints dynamically determined based on input variables.
    """
    # Default thresholds (used as base values)
    security_threshold = (6, 10)
    intrusiveness_threshold = (0, 5)
    privacy_threshold = (5, 10)
    accuracy_threshold = (6, 10)

    # Retrieve contextual data
    last_login_time = context.get('device_usage', {}).get('last_login_time')
    recent_failed_attempts = context.get('recent_failed_attempts', 0)
    request_security_rating = context.get('request_security_rating', 'medium')

    # Adjust constraints dynamically
    # Security constraints
    if recent_failed_attempts > 2:
        security_threshold = (8, 10)  # Require higher security due to recent failed attempts

    if request_security_rating == 'high':
        security_threshold = (8, 10)
        privacy_threshold = (7, 10)

    # Adjust intrusiveness constraints based on time since the last login
    if last_login_time:
        # Calculate time since last login in hours
        from datetime import datetime
        time_since_last_login = (datetime.now() - datetime.fromisoformat(last_login_time[:-1])).total_seconds() / 3600

        if time_since_last_login < 1:
            intrusiveness_threshold = (0, 2)  # Lower intrusiveness shortly after logging in
        else:
            intrusiveness_threshold = (0, 4)

    # Adjust accuracy thresholds if security rating is high
    if request_security_rating == 'high':
        accuracy_threshold = (8, 10)

    # Return the attribute constraints
    return {
        'Security': security_threshold,
        'Intrusiveness': intrusiveness_threshold,
        'Privacy': privacy_threshold,
        'Accuracy': accuracy_threshold
    }


if __name__ == '__main__':
    # Example factor modules
    factor_modules = ['facial_recognition', 
                      'fingerprint', 
                      'password', 
                      'geolocation', 
                      'battery_information',
                      'ip_address',
                      'network_flow_statistics',
                      'timezone',
                      'screen_frame_resolution']

    # Run the evaluation and selection process
    solutions = evaluate_and_select_factors("variables.json", factor_modules, determine_attribute_constraints)
    print("Solutions:", solutions)