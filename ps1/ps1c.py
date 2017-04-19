#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:06:07 2017

@author: Leo
"""

'''
Defined Variables:
******************
total_cost: Total house cost
portion_down_payment: portion of cost needed for down payment (0.25 assumed)
current_savings: current savings (assumed $0)
r: annual return rate (assumed 0.04)
annual_salary: annual salary
portion_saved: portion of salary saved each month (e.g. 0.1)
semi_annual_raise: decimal amount of raise every 6 months

At the end of each month, savings increase by return on investment + percentage
of monthly salary.
'''

# User inputs
annual_salary = float(input('Enter the starting salary: '))

# Initialize variables
possible = True
start_range = 0
num_decimals = 2
end_range = 100 * 10**num_decimals
total_cost = 1E6
semi_annual_raise = 0.07
r = 0.04
total_years = 3
savings_margin = 100.0
total_months = total_years * 12
monthly_return_rate = r / 12
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost

# Calculations
def get_savings(savings_integer, annual_salary_variable):
    current_savings = 0.0
    monthly_salary = annual_salary_variable / 12.0
    monthly_saved = monthly_salary * savings_integer / end_range
    
    for month_count in range(1, total_months + 1):
        monthly_return = monthly_return_rate * current_savings
        current_savings += monthly_return + monthly_saved
    
        if(month_count % 6 == 0):
            annual_salary_variable *= (1 + semi_annual_raise)
            monthly_salary = annual_salary_variable / 12
            monthly_saved = monthly_salary * savings_integer / end_range
    
    return current_savings - down_payment

a = 0
a_margin = get_savings(a, annual_salary)
b = end_range
b_margin = get_savings(b, annual_salary)

# Check if it's possible
if(b_margin < 0):
    print('It is not possible to pay the down payment in ' + str(total_years) + ' years.')
    possible = False

# If possible, perform bisecion method
bisection_steps = 1
c = round((a + b) / 2)
c_margin = get_savings(c, annual_salary)
while(abs(c_margin) >= savings_margin and possible):
    bisection_steps += 1
    
    if(a_margin * c_margin < 0):
        b = c
    elif(b_margin * c_margin < 0):
        a = c
    else:
        print('No sign change! Something is wrong.')
        
    c = round((a + b) / 2)
    c_margin = get_savings(c, annual_salary)
    
# Output
if(possible):
    print('Best savings rate: ' + str(c / end_range))
    print('Steps in bisection search: ' + str(bisection_steps))
