from modalities.facial_recognition import FacialRecognition
from modalities.ip_continuity import IPAddressContinuity

# Environment and variables for office access
office_environment = {'dynamic_ip': False, 'ip_change_frequency': 'low', 'ip_stability': True, 'lighting_adaptability': True}
office_device = {'data_encryption': True, 'hardware_capability': 'advanced', 'encryption_level': 'high'}
office_variables = {'vpn_or_proxy_use': False, 'network_security_measures': True, 'user_consent': True, 'user_consent_for_ip_tracking': True, 'expert_opinion_on_security': 0.7, 'demographic_flexibility': True}

# Environment and variables for café access
cafe_environment = {'dynamic_ip': True, 'ip_change_frequency': 'high', 'ip_stability': False}
cafe_device = {'data_encryption': True, 'hardware_capability': 'standard', 'encryption_level': 'medium'}
cafe_variables = {'vpn_or_proxy_use': True, 'network_security_measures': False, 'user_consent': False, 'user_consent_for_ip_tracking': False, 'expert_opinion_on_security': 0.3, 'demographic_flexibility': True}

# Instantiate modalities for office access
office_facial_recognition = FacialRecognition(office_environment, office_device, office_variables)
office_ip_continuity = IPAddressContinuity(office_environment, office_device, office_variables)

# Instantiate modalities for café access
cafe_facial_recognition = FacialRecognition(cafe_environment, cafe_device, cafe_variables)
cafe_ip_continuity = IPAddressContinuity(cafe_environment, cafe_device, cafe_variables)

# Print attribute scores for both modalities in both environments
print("Office Access - Facial Recognition Attributes:", office_facial_recognition.calculate_attributes())
print("Office Access - IP Address Continuity Attributes:", office_ip_continuity.calculate_attributes())
print("---")
print("Café Access - Facial Recognition Attributes:", cafe_facial_recognition.calculate_attributes())
print("Café Access - IP Address Continuity Attributes:", cafe_ip_continuity.calculate_attributes())
