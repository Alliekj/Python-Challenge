import csv

filename = "election_data.csv"


# Initialize variables
total_votes = 0
candidate_votes = {}

with open(filename, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)  # Skip header

    # Calculate total votes and votes per candidate
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on popular votes
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the analysis results to a text file
output_filename = "analysis/election_results.txt"
with open(output_filename, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
