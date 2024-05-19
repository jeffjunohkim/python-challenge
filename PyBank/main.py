import os
import csv

# Construct the relative paths
csv_path = r'python-challenge\PyBank\Resources\budget_data.csv'
output_path = r'python-challenge\PyBank\analysis\financial_analysis.txt'

# Initialize variables
total_months = 0
net_total_amount = 0
monthly_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', float('inf')]

# Open the CSV file
with open(csv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    # Read the first row to handle the initial values
    first_row = next(csvreader)
    total_months += 1
    net_total_amount += int(first_row[1])
    prev_net = int(first_row[1])
    
    # Iterate through each row after the header and first row
    for row in csvreader:
        total_months += 1
        net_total_amount += int(row[1])
        
        # Calculate change from previous month
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        monthly_changes.append(net_change)
        
        # Calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        # Calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
    # Calculate the average net change
    average_change = sum(monthly_changes) / len(monthly_changes)

# Print out the analysis to match the expected results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to the text file
with open(output_path, mode='w', newline='') as textfile:
    # Write the headers and data
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total_amount}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print("Financial analysis exported to text file successfully.")