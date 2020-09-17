import os
import csv

# Create 2 lists (date and profit_loss)
date = []
profit_loss = []

# Points to csv file containing the csv dataset
budget = os.path.join ("Resources", "budget_data.csv")

# Read each row of the csv dataset into the respective above lists based on column location 
# Eliminate header in csv file
with open(budget, "r") as budgetfile:
    budget_data = csv.reader(budgetfile, delimiter = ",")
    headers = next(budget_data)
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])

# Calculate total number of months by counting the length of the date list and converting that to an integer format
total_months = int(len(date))

# net is sum of profits and losses through all months.
# loss and profit lists are created to initially sort the values as a positive (meaning profit) or a negative number (meaning loss).
# profit_loss 2 lists stores each profit or loss dollar value as a number.
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
    
# Average, min and max using above lists.           
average_change = round(net / total_months, 2)
greatest_decrease = min(loss)
greatest_increase = max(profit)

# Create dictionary to connect each date with the respective profit/lass dollar value
summary = {profit_loss2[i] : date[i] for i in range(len(profit_loss2))}

for num, day in summary.items():
    if num == greatest_decrease:
        date_decrease = day
    if num == greatest_increase:
        date_increase = day    

# Display results in terminal using the associated variables from above
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total months: {total_months}")
print(f"Net Earnings: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
print(f"Greatest Decrease in Losses: {date_decrease} (${greatest_decrease})")

# Display results in a txt file using the associated variables from above
summary = os.path.join ("Analysis", "Budgetsummary.txt")
with open(summary,"w") as report:
    report.write("Financial Analysis \n")
    report.write("---------------------------------------- \n")
    report.write(f"Total months: {total_months} \n")
    report.write(f"Net Earnings: ${net} \n")
    report.write(f"Average Change: ${average_change} \n")    
    report.write(f"Greatest Increase in Profits: {date_increase} (${greatest_increase}) \n")    
    report.write(f"Greatest Decrease in Losses:  {date_decrease} (${greatest_decrease}) \n")    