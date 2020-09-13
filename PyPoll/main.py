import csv
import os

voterid = []
county = []
candidate = []


poll_data = os.path.join("Resources", "election_data.csv")

with open(poll_data, "r") as pollfile:
    election_data = csv.reader(pollfile, delimiter = ",")
    headers = next(election_data)
    for row in election_data:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_votes = len(voterid)

khan_sum = 0
correy_sum = 0
li_sum = 0
otooley_sum = 0
for person in candidate:
    if person == "Khan":
        khan_sum = khan_sum + 1
    elif person == "Correy":    
        correy_sum = correy_sum + 1
    elif person == "Li":
        li_sum = li_sum + 1
    elif person == "O'Tooley":
        otooley_sum = otooley_sum + 1
    else:
        other_sum = other_sum + 1

percentage_khan = round(khan_sum / total_votes * 100, 0)
percentage_correy = round(correy_sum / total_votes * 100, 0)
percentage_li = round(li_sum / total_votes * 100, 0)
percentage_otooley = round(otooley_sum / total_votes * 100, 0)

person = ("KHAN", "CORREY", "LI", "O'Tooley")
personal_votes = (percentage_khan, percentage_correy, percentage_li, percentage_otooley)
winner_votes = max(personal_votes)
winner = {person[i] : personal_votes[i] for i in range(len(personal_votes))}
for name, num in winner.items():
    if num == winner_votes:
        final_winner = name

print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
print(f"KHAN {percentage_khan}% ({khan_sum})")
print(f"CORREY {percentage_correy}% ({correy_sum})")
print(f"LI {percentage_li}% ({li_sum})")
print(f"O'TOOLEY {percentage_otooley}% ({otooley_sum})")
print(f"{final_winner} is the WINNER!")

summary = os.path.join ("Analysis", "electionsummary.csv")

writer = []
with open(summary,"w") as report:
    writer = csv.writer(report, delimiter = " ")
    writer.writerow("Election Results")
    writer.writerow("----------------------------------------")
    writer.writerow(f"Total Votes: {total_votes}")
    writer.writerow("----------------------------------------")
    writer.writerow(f"KHAN {percentage_khan}% ({khan_sum})")
    writer.writerow(f"CORREY {percentage_correy}% ({correy_sum})")
    writer.writerow(f"LI {percentage_li}% ({li_sum})")  
    writer.writerow(f"O'TOOLEY {percentage_otooley}% ({otooley_sum})")
    writer.writerow(f"{final_winner} is the WINNER!") 