import csv
import os

# Define the file path for the election_data.csv file
csv_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winning_count = 0

# Open and read the CSV file
with open(csv_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    # Process each row in the CSV
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Candidate name is in the third column

        # Add to candidate's vote count or initialize it
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate the percentage of votes for each candidate and determine the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    # Determine the winner based on vote count
    if votes > winning_count:
        winning_count = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")