def calculate_budget(income, expenses):
    savings = income - expenses
    if savings > income * 0.2:
        return "Great. We are saving good amount of money."
    elif savings > income * 0.1:
        return "Good.The saving are good, need some budgeting. "
    else:
        return "Poor, Our svaings are too low, need to follow budgeting."

def track_expenses(expenses_list):
    total_expenses = sum(expenses_list)
    return f"Total Expenses: Rs.{total_expenses}"

def recommend_savings(income, expenses):
    savings = income - expenses
    if savings > 0:
        return f"You can save Rs.{savings} this month. Consider setting a goal."
    else:
        return "You're overspending. Reduce expenses to save."


income = 50000
expenses_list = [12000, 8000, 6000, 4000, 3000] 
expenses = sum(expenses_list)

budget_suggestion = calculate_budget(income, expenses)
expense_tracking = track_expenses(expenses_list)
savings_recommendation = recommend_savings(income, expenses)


print(budget_suggestion)
print(expense_tracking)
print(savings_recommendation)
