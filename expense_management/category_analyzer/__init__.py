class CategoryAnalyzer:
    def __init__(self):
        self.categories = {
            ' Groceries': 0.2, 
            'Utilities': 0.15,
            # ... other categories with their usual percentages
        }

    def analyze(self, expenses):
        categorized = {}
        for expense in expenses:
            category = self._determine_category(expense['description'])
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(expense)
        return categorized

    def _determine_category(self, description):
        # Simple initial categorization
        description_lower = description.lower()
        for cat in self.categories:
            if cat.lower() in description_lower:
                return cat
        return 'Other'