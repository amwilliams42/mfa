from modalities.modality import AuthenticationModality

class FacialRecognition(AuthenticationModality):
    def accuracy(self):
        # Assume FRR is a base attribute of the device, lower is better
        base_accuracy = 1 - self.device.get('FRR', 0.05)  # Default FRR to 5%

        # Adjust accuracy based on lighting conditions
        lighting_condition = self.environment.get('lighting', 'optimal')
        lighting_adjustment = {
            'optimal': 0.00,  # No adjustment needed
            'bright': -0.05,  # Slight decrease in accuracy
            'dim': -0.10,  # Moderate decrease in accuracy
            'dark': -0.20  # Significant decrease in accuracy
        }
        lighting_factor = lighting_adjustment.get(lighting_condition, -0.10)  # Default to 'dim' conditions

        # Further adjustments based on hypothetical attributes:
        # Camera quality (high, medium, low)
        camera_quality = self.device.get('camera_quality', 'medium')
        quality_adjustment = {
            'high': 0.05,  # Increase in accuracy for high-quality cameras
            'medium': 0.00,  # No adjustment needed
            'low': -0.05  # Decrease in accuracy for low-quality cameras
        }
        quality_factor = quality_adjustment.get(camera_quality, 0.00)

        # User's position relative to camera (ideal, acceptable, poor)
        user_position = self.variables.get('user_position', 'ideal')
        position_adjustment = {
            'ideal': 0.00,  # No adjustment needed
            'acceptable': -0.05,  # Slight decrease in accuracy
            'poor': -0.10  # Moderate decrease in accuracy
        }
        position_factor = position_adjustment.get(user_position, -0.05)  # Default to 'acceptable'

        # Calculate the final accuracy
        final_accuracy = base_accuracy + lighting_factor + quality_factor + position_factor
        return max(min(final_accuracy, 1.0), 0.0)  # Ensure the accuracy is within [0, 1]

    def intrusiveness(self):
    # Expert value for the modality's intrusiveness, on a scale from 0 to 1
        modality_intrusiveness = 0.8  # Example: 0.8 for facial recognition

        # Location context impact
        location = self.variables.get('user_location', 'private')  # Default to 'private'
        location_impact = {
            'home': -0.5,  # Less intrusive at home
            'office': 0.0,  # Neutral in an office
            'public': 0.5,  # More intrusive in public places like coffee shops
        }
        location_factor = location_impact.get(location, 0.0)  # Default to 0 for unknown locations

        # Calculate final intrusiveness
        final_intrusiveness = modality_intrusiveness + location_factor

        return max(min(final_intrusiveness, 1.0), 0.0)  # Ensure within [0, 1]


    def security(self):
        # Expert value for modality's security, on a scale from 0 to 1
        modality_security = 0.7  # Example: 0.7 for facial recognition, higher is more secure

        # Impact of FAR (lower FAR means higher security)
        far_impact = 1 - self.device.get('FAR', 0.01)  # Default FAR to 1%

        # Encryption level impact
        encryption_level = self.device.get('encryption_level', 'none')  # Default to 'none'
        encryption_impact = {
            'none': -0.2,
            'low': -0.1,
            'high': 0.1,
        }
        encryption_factor = encryption_impact.get(encryption_level, 0.0)  # Default to 0 for unknown

        # Trustworthiness of the connection
        connection_trust = self.environment.get('connection_trust', 'low')  # Default to 'low'
        connection_impact = {
            'low': -0.1,
            'medium': 0.0,
            'high': 0.1,
        }
        connection_factor = connection_impact.get(connection_trust, 0.0)  # Default to 0 for unknown

        # Calculate final security
        final_security = modality_security + far_impact + encryption_factor + connection_factor
        return max(min(final_security, 1.0), 0.0)  # Ensure within [0, 1]


    def privacy(self):
        # Data encryption level impact
        encryption_level = self.device.get('encryption_level', 'none')  # Assume 'none' as default
        encryption_impact = {
            'none': -0.3,  # Significant negative impact on privacy
            'low': -0.1,
            'high': 0.2,  # Positive impact on privacy
        }
        encryption_factor = encryption_impact.get(encryption_level, -0.1)  # Default to low if unknown

        # Data storage location impact
        storage_location = self.device.get('storage_location', 'remote')  # Assume 'remote' as default
        storage_impact = {
            'local': 0.2,  # Local storage is more private
            'remote': -0.2,  # Remote storage is less private due to potential access points
        }
        storage_factor = storage_impact.get(storage_location, -0.2)  # Default to remote if unknown

        # Biometric data reuse potential
        reuse_potential = self.variables.get('reuse_potential', 'high')  # Assume 'high' as default
        reuse_impact = {
            'low': 0.1,  # Low potential for reuse is better for privacy
            'high': -0.2,  # High potential for reuse is worse for privacy
        }
        reuse_factor = reuse_impact.get(reuse_potential, -0.2)  # Default to high if unknown

        # Calculate final privacy score
        final_privacy = encryption_factor + storage_factor + reuse_factor
        return max(min(final_privacy, 1.0), 0.0)  # Ensure within [0, 1]


    def utility(self):
        # Adaptability to various lighting conditions
        lighting_adaptability = self.environment.get('lighting_adaptability', True)  # Assume good adaptability
        lighting_factor = 0.2 if lighting_adaptability else -0.2

        # Flexibility for different demographic groups
        demographic_flexibility = self.variables.get('demographic_flexibility', True)  # Assume flexible
        demographic_factor = 0.2 if demographic_flexibility else -0.2

        # Resilience to spoofing attempts
        spoofing_resilience = self.device.get('spoofing_resilience', True)  # Assume resilient
        spoofing_factor = 0.2 if spoofing_resilience else -0.2

        # General ease of use
        ease_of_use = self.variables.get('ease_of_use', True)  # Assume easy to use
        ease_factor = 0.2 if ease_of_use else -0.2

        # Calculate final utility score
        final_utility = lighting_factor + demographic_factor + spoofing_factor + ease_factor
        return max(min(final_utility, 1.0), 0.0)  # Ensure within [0, 1]


    def speed(self):
        # Hardware capability (assume 'standard', 'advanced')
        hardware_capability = self.device.get('hardware_capability', 'standard')
        hardware_factor = {
            'standard': 0.0,  # No adjustment for standard hardware
            'advanced': -0.2  # Faster with advanced hardware
        }.get(hardware_capability, 0.0)

        # Algorithm efficiency ('high', 'medium', 'low')
        algorithm_efficiency = self.device.get('algorithm_efficiency', 'medium')
        efficiency_factor = {
            'high': -0.2,  # Less time, more efficient
            'medium': 0.0,
            'low': 0.2  # More time, less efficient
        }.get(algorithm_efficiency, 0.0)

        # Pre-processing requirement ('none', 'minimal', 'extensive')
        preprocessing_requirement = self.device.get('preprocessing_requirement', 'none')
        preprocessing_factor = {
            'none': -0.1,
            'minimal': 0.0,
            'extensive': 0.2  # Slower if extensive pre-processing is needed
        }.get(preprocessing_requirement, 0.0)

        # Calculate final speed score (negative because lower values are faster)
        final_speed = hardware_factor + efficiency_factor + preprocessing_factor
        # Convert speed to a positive scale where higher is better
        return 1.0 + final_speed  # Adjust to ensure within [0, 1], if needed
