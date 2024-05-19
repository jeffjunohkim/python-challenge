import os
import csv

# Get the current working directory
current_dir = os.getcwd()

# Construct the relative paths
csv_path = r'python-challenge\PyPoll\Resources\election_data.csv'
output_path = r'python-challenge\PyPoll\analysis\election_results.txt'

# Initialize variables
total_votes = 0
candidates = {}
winner = ''
winner_votes = 0

# Open the CSV file
try:
    with open(csv_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Skip the header
        next(csvreader)
        
        # Process each row
        for row in csvreader:
            total_votes += 1
            candidate_name = row[2]
            
            # If the candidate is in the dictionary, increment their vote count
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                # If not, add them to the dictionary
                candidates[candidate_name] = 1

    # Determine the winner and calculate the percentage of votes
    for candidate, votes in candidates.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
        candidates[candidate] = {'votes': votes, 'percentage': (votes / total_votes) * 100}

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, data in candidates.items():
        print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Save the results to a text file
    with open(output_path, mode='w', newline='') as textfile:
        textfile.write("Election Results\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("-------------------------\n")
        for candidate, data in candidates.items():
            textfile.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("-------------------------\n")

    print("Election analysis exported to text file successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please ensure the CSV file exists at the specified path.")
