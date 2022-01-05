salary = float(input("Enter your annual salary: "))
portion_down_payment = 0.25
current_savings = 0
save = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
cost_paid = total_cost * portion_down_payment
total_cost = total_cost - cost_paid

def totalMonths(total_cost, save, current_savings):
    total_cost = total_cost

