# Financial Analysis Project

## Overview
This Python script is designed to automate the analysis of financial records. It calculates total months, net total amount of profit/losses, average changes in profit/losses, and identifies the greatest increase and decrease in profits over a given period.

## Features
- **Total Months Calculation**: Counts the total number of months included in the dataset.
- **Net Total Amount Calculation**: Sums up the total profit/loss over the entire period.
- **Monthly Changes Calculation**: Determines the changes in profit/loss over the entire period and calculates the average of those changes.
- **Greatest Increase/Decrease Identification**: Identifies the greatest increase and decrease in profits (date and amount) over the entire period.

## Usage
1. Ensure the `budget_data.csv` file is located in the `PyBank\Resources` directory.
2. Run the script using a Python interpreter.
3. The script will output the financial analysis to the console and export it to a text file in the `PyBank\analysis` directory.

## Output
The script prints out the analysis with the following format:

Financial Analysis
Total Months: [total_months]
Total: [nett​otala​mount]
AverageChange:[average_change]
Greatest Increase in Profits: [greatest_increase_month] ([greatesti​ncreasea​mount])
GreatestDecreaseinProfits:[greatestd​ecreasem​onth]([greatest_decrease_amount])

It also saves this analysis to a text file named `financial_analysis.txt`.

## Requirements
- Python 3
- CSV file named `budget_data.csv` with the columns "Date" and "Profit/Losses"


