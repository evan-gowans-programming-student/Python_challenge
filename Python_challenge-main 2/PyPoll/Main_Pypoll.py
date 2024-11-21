import csv
import os

# Define the file paths
csv_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_results.txt")  # Output file path

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

# Prepare the results
results_output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Calculate the percentage of votes for each candidate and determine the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    results_output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    # Determine the winner based on vote count
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Add the winner to the results
results_output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results to the terminal
print(results_output)

# Export the results to a text file
with open(output_path, mode='w') as output_file:
    output_file.write(results_output)