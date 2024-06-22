monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))
Interest_R = 0.05

monthly_savings = int(monthly_income - monthly_expenses)
monthly_savings=float(monthly_income)-float(monthly_expenses)
projected_Savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_Savings}.")

