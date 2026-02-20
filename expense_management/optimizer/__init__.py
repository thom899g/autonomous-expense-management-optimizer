from .category_analyzer import CategoryAnalyzer
from .expense_negotiator import ExpenseNegotiator
from .cashflow_analyzer import CashflowAnalyzer

class ExpenseOptimizer:
    def __init__(self):
        self.category_analyzer = CategoryAnalyzer()
        self.expense_negotiator = ExpenseNegotiator()
        self.cashflow_analyzer = CashflowAnalyzer()

    def optimize(self, expenses):
        categories = self.category_analyzer.analyze(expenses)
        optimized_expenses = self.expense_negotiator.negotiate(categories)
        cashflow_impact = self.cashflow_analyzer.predict(optimized_expenses)
        return {
            'categories': categories,
            'negotiated_expenses': optimized_expenses,
            'cashflow_impact': cashflow_impact
        }