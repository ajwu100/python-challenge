import csv
import os

# Create 3 lists (voterid, county and candidate)
voterid = []
county = []
candidate = []

# Points to csv file containing the csv dataset
poll_data = os.path.join("Resources", "election_data.csv")

# Eliminate header in csv file
# Read each row of the csv dataset into the respective above lists based on column location 
with open(poll_data, "r") as pollfile:
    election_data = csv.reader(pollfile, delimiter = ",")
    headers = next(election_data)
    for row in election_data:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
# Calculate total number of votes by counting the length of the voterid list and converting that to an integer format
total_votes = len(voterid)

# Sum up the number of votes for each candidate using a loop function applied onto the candidate list (created above)
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

# Calculate percentage of votes each candidate received out of total number of votes
percentage_khan = round(khan_sum / total_votes * 100, 0)
percentage_correy = round(correy_sum / total_votes * 100, 0)
percentage_li = round(li_sum / total_votes * 100, 0)
percentage_otooley = round(otooley_sum / total_votes * 100, 0)

# Create dictionary to connect each candidate with his/her respective percentage value.
# Winner has the highest or max percentage.
person = ("KHAN", "CORREY", "LI", "O'Tooley")
personal_votes = (percentage_khan, percentage_correy, percentage_li, percentage_otooley)
winner_votes = max(personal_votes)
winner = {person[i] : personal_votes[i] for i in range(len(personal_votes))}
for name, num in winner.items():
    if num == winner_votes:
        final_winner = name

# Display results in terminal using the associated variables from above
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
print(f"KHAN {percentage_khan}% ({khan_sum})")
print(f"CORREY {percentage_correy}% ({correy_sum})")
print(f"LI {percentage_li}% ({li_sum})")
print(f"O'TOOLEY {percentage_otooley}% ({otooley_sum})")
print(f"{final_winner} is the WINNER!")

# Display results in a txt file using the associated variables from above
summary = os.path.join ("Analysis", "electionsummary.txt")

with open(summary,"w") as report:
    report.write("Election Results \n")
    report.write("---------------------------------------- \n")
    report.write(f"Total Votes: {total_votes} \n")
    report.write("---------------------------------------- \n")
    report.write(f"KHAN {percentage_khan}% ({khan_sum}) \n")
    report.write(f"CORREY {percentage_correy}% ({correy_sum}) \n")
    report.write(f"LI {percentage_li}% ({li_sum}) \n")  
    report.write(f"O'TOOLEY {percentage_otooley}% ({otooley_sum}) \n")
    report.write(f"{final_winner} is the WINNER! \n") 