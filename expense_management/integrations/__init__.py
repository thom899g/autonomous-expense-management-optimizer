class EcosystemIntegration:
    def __init__(self):
        self.knowledge_base = None  # Will be injected or set via dependency injection
        self.dashboard = None       # Similarly, dependencies to be managed

    def update_knowledge_base(self, data):
        if self.knowledge_base:
            self.knowledge_base.update('expense_data', data)

    def push_to_dashboard(self, data):
        if self.dashboard:
            self.dashboard.display(data)