import os
import csv

date = []
profit_loss = []

budget = os.path.join ("Resources", "budget_data.csv")

with open(budget, "r") as budgetfile:
    budget_data = csv.reader(budgetfile, delimiter = ",")
    headers = next(budget_data)
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])


total_months = int(len(date))

net = 0
loss = []
profit = []

for num in profit_loss:
    dollar = float(num)
    net = round(net + dollar, 2)
    if dollar < 0:
        loss.append(dollar)
    if dollar > 0:    
        profit.append(dollar)
    
           
average_change = round(net / total_months, 2)
greatest_decrease = min(loss)
greatest_increase = max(profit)
#gd = int(greatest_decrease)
#gi = int(greatest_increase)
#print(gd)
#print(gi)
#index_d = profit_loss.index(gd)
#index_i = profit_loss.index(gi)


print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total months: {total_months}")
print(f"Net Earnings: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:(${greatest_increase})")
print(f"Greatest Decrease in Losses: (${greatest_decrease})")