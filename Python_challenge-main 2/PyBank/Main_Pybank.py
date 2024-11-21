import csv
import os

# Define the file path for the budget_data.csv file
csv_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "financial_analysis.txt")  # Path for the output text file

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
months = []

# Open and read the CSV file
with open(csv_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract date and profit/loss
        date = row[0]
        profit = int(row[1])

        # Add to total months and net total
        total_months += 1
        net_total += profit

        # Calculate change from previous month
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            months.append(date)
        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Find the greatest increase and decrease in profits
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0
greatest_increase_month = months[changes.index(greatest_increase)] if changes else ''
greatest_decrease_month = months[changes.index(greatest_decrease)] if changes else ''

# Prepare the analysis output
analysis_output = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the results to the terminal
print(analysis_output)

# Export the results to a text file
with open(output_path, mode='w') as output_file:
    output_file.write(analysis_output)