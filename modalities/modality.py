class AuthenticationModality:
    def __init__(self, environment, device, variables):
        self.environment = environment
        self.device = device
        self.variables = variables

    def accuracy(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def intrusiveness(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def security(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def privacy(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def utility(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def speed(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def calculate_attributes(self):
        return (
            self.accuracy(),
            self.intrusiveness(),
            self.security(),
            self.privacy(),
            self.utility(),
            self.speed(),
        )