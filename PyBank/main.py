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
profit_loss2 =[]

for num in profit_loss:
    dollar = float(num)
    profit_loss2.append(dollar)
    net = round(net + dollar, 2)
    if dollar < 0:
        loss.append(dollar)
    if dollar > 0:    
        profit.append(dollar)
    
           
average_change = round(net / total_months, 2)
greatest_decrease = min(loss)
greatest_increase = max(profit)

summary = {profit_loss2[i] : date[i] for i in range(len(profit_loss2))}

for num, day in summary.items():
    if num == greatest_decrease:
        date_decrease = day
    if num == greatest_increase:
        date_increase = day    

print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total months: {total_months}")
print(f"Net Earnings: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
print(f"Greatest Decrease in Losses: {date_decrease} (${greatest_decrease})")

summary = os.path.join ("Analysis", "Budgetsummary.csv")

writer = []
with open(summary,"w") as report:
    writer = csv.writer(report, delimiter = " ")
    writer.writerow("Financial Analysis")
    writer.writerow("----------------------------------------")
    writer.writerow(f"Total months: {total_months}")
    writer.writerow(f"Net Earnings: ${net}")
    writer.writerow(f"Average Change: ${average_change}")    
    writer.writerow(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")    
    writer.writerow(f"Greatest Decrease in Losses:  {date_decrease} (${greatest_decrease})")    