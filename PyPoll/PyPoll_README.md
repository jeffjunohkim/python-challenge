# Election Analysis Project

## Overview
This Python script is developed to modernize the vote-counting process for a small, rural town. It analyzes a set of poll data and calculates various election statistics, including the total number of votes, the percentage of votes each candidate won, and the winner of the election based on the popular vote.

## Features
- **Total Vote Count**: Calculates the total number of votes cast in the election.
- **Candidate Vote Summary**: Generates a complete list of candidates who received votes and the total number of votes each candidate won.
- **Vote Percentage**: Computes the percentage of votes each candidate won.
- **Election Winner**: Determines the winner of the election based on the popular vote.

## Usage
1. Place the `election_data.csv` file in the `PyPoll/Resources` directory.
2. Run the script using a Python interpreter.
3. The script will output the election results to the console and save them to a text file.

## Output
The script outputs the election results in the following format:

Election Results
Total Votes: [total_votes]
…
Winner: [winner_name]

The results are also saved to a text file named `election_results.txt` in the `PyPoll/analysis` directory.

## Requirements
- Python 3
- CSV file named `election_data.csv` with the columns "Voter ID", "County", and "Candidate"

## Code Source
- Learning Assistant
- GitHub location: https://github.com/jeffjunohkim/python-challenge.git
