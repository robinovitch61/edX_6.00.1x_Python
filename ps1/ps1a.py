#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:29:103 2017

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

At the end of each month, savings increase by return on investment + percentage
of monthly salary.
'''

# User inputs
annual_salary = float(input('Enter your starting salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))


# Initialize variables
r = 0.04
portion_down_payment = 0.25
monthly_return_rate = r / 12
down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved


# Calculations
current_savings = 0
months = 0

while(current_savings < down_payment):
    months += 1
    monthly_return = monthly_return_rate * current_savings
    current_savings += monthly_return + monthly_saved
    
    
# Output
print('Number of months: ' + str(months))


