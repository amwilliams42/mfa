from modalities.modality import AuthenticationModality


class IPAddressContinuity(AuthenticationModality):
    def accuracy(self):
        # IP address continuity is less accurate due to dynamic IP allocation, VPNs, and proxies
        dynamic_ip = self.environment.get('dynamic_ip', True)
        vpn_or_proxy_use = self.variables.get('vpn_or_proxy_use', False)
        if dynamic_ip or vpn_or_proxy_use:
            return 0.3  # Lower accuracy due to changeable IPs and anonymizing services
        return 0.7  # Higher accuracy in stable IP environments without VPN/proxy use

    def intrusiveness(self):
        # Non-intrusive as it passively uses existing IP information without requiring user action
        return 0.1  # Low intrusiveness score

    def security(self):
        # Security depends on additional measures like network monitoring and anomaly detection
        network_security_measures = self.variables.get('network_security_measures', False)
        if network_security_measures:
            return 0.7  # Higher security with robust network monitoring
        return 0.4  # Lower security without additional network security measures

    def privacy(self):
        # Privacy concerns are significant due to tracking and storing IP addresses
        user_consent = self.variables.get('user_consent', False)
        data_encryption = self.device.get('data_encryption', False)
        if user_consent and data_encryption:
            return 0.8  # Higher privacy with consent and encrypted data storage
        return 0.2  # Lower privacy without user consent and data encryption

    def utility(self):
        # Utility is high in environments where IP continuity is a reliable indicator of user identity
        ip_change_frequency = self.environment.get('ip_change_frequency', 'high')
        if ip_change_frequency == 'low':
            return 0.8  # High utility in stable IP environments
        return 0.3  # Low utility in environments with frequent IP changes

    def speed(self):
        # IP address checks are fast, requiring minimal processing
        return 0.9  # High speed due to the simplicity of the check
