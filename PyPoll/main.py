# Import Modules
import os
import csv

# Define variables
votes = 0
candidates = []
votesByCandidate = []

# Import CSV
csvPath = os.path.join('Resources', 'election_data.csv')

# Read CSV
with open(csvPath) as data:

    # Parse CSV
    reader = csv.reader(data, delimiter=",")

    # Skip header
    next(reader, None)

    # Loop through CSV
    for row in reader:

        # Increment votes
        votes += 1

        candidate = row[2]

        # Put candidate in the candidates list if they are not already there
        if candidate not in candidates:
            candidates.append(candidate)
            votesByCandidate.append(0)

        # Find the correct index to record the vote
        index = candidates.index(candidate)
        votesByCandidate[index] += 1

# Calculate percentages for each candidate
percentages = []
for i in range(len(candidates)):
    percentages.append((votesByCandidate[i]/votes)*100)

# Determine the winner by finding the index for the largest number of votes, and accessing that index in the candidates array
winner = candidates[votesByCandidate.index(max(votesByCandidate))]

# Programatically make a string containing each candidate, their percentage of votes, and their total votes
candidateTotals = ""
for i in range(len(candidates)):
    candidateTotals += f"{candidates[i]}: {percentages[i]:.2f}% ({votesByCandidate[i]})"
    if i < 2:
        candidateTotals += "\n"

# Print analysis and output to text file
analysis = f"""
Election Results
-------------------------
Total votes: {votes}
-------------------------
{candidateTotals}
-------------------------
Winner: {winner}
-------------------------
"""

print(analysis)

output = open("Analysis/results.txt", "w")
output.write(analysis)
output.close()
