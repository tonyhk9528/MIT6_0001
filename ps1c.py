#input
annual_salary = float (input('Enter your annual salary:'))
total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0
max_current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
semi_annual_raise = .07

high = 10000 #100%
low = 0 #0
portion_saved = (high + low) / 2.0 #50% first guess

epsilon = 100
steps = 0
for months in range(1, 37):
    max_current_savings = max_current_savings * (1 + r / 12) + monthly_salary * 1
    if months % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)
if down_payment > max_current_savings:
    print ('It is not possible to pay the down payment in three years.')
else:
    steps += 1
    for months in range(1, 37):
        current_savings = current_savings * (1 + r / 12) + monthly_salary * portion_saved
        if months % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    while abs (current_savings - down_payment) >= epsilon:
        steps += 1
        if down_payment > current_savings:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high + low) / 2
        current_savings = 0
        monthly_salary = annual_salary / 12
        for months in range(1, 37):
            current_savings = current_savings * (1 + r / 12) + monthly_salary * portion_saved/10000
            if months % 6 == 0:
                monthly_salary = monthly_salary * (1 + semi_annual_raise)
                
#output                
print ('Best savings rate: ' + str(round(portion_saved)/10000))
print ('Steps in bisection search: ' + str(steps))
