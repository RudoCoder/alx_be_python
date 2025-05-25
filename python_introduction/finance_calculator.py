#Personal info
name = str(input('Please enter your name: '))
age = int(input("Please enter your age: "))
Job_title = str(input("Please enter your job title: "))

#Salary info
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05
Projected_Savings = monthly_savings * 12 + int(monthly_savings * 12 * 0.05)

#print results
print(f"Your monthly savngs is ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")