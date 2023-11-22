#input
annual_salary = float (input('Enter your annual salary:'))
portion_saved = float (input ("Enter the percent of your salary to save, as a decimal:"))
total_cost = float (input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal:"))
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

month = 0
while current_savings < down_payment:
    current_savings += monthly_salary * portion_saved + (current_savings*r/12)
    month +=  1
    if month % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

#output
print ("Number of months:",month)
