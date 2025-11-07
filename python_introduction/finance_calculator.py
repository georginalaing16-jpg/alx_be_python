# Prompt user to insert their monthly income
monthly_income = int(input("Enter your monthly income: "))
# Prompt user to insert their total monthly expenses
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses
# Print the result
print("Your monthly savings are $" + str(monthly_savings)+".")
# Assume a simple annual interest of 5%(0.05)
# Calculate the projected savings after one year with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# Print the projected savings after one year
print("Projected savings after one year, with interest, is: $" + str(round(projected_savings))+".")
