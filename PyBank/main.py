#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""Python-Homework: Finacial Analysis.
Creates a Python script for analyzing the financial records of your 
company using the budget_data.csv file. This file contains full 
financial dataset of the company. This dataset is composed of two
columns, Date & Profit/Losses.

The script analyzes the records to calculate:

1. The total number of months included in the dataset.
2. The net total amount of Profit/Losses over entire period.
3. The average of the changes in Profit/Losses over entire period.
4. The greatest increase in profits (date & amount) over entire period.
5. The greatest decrease in losses (date & amount) over entire period.


It prints the summary of the financial analysis to the terminal and 
exports a text file with the results.
"""

# Function average_profit_change determines avg_change from inputlist,
# based on col index to get each delta & num_months the values span
def average_profit_change(inputlist, change_col, num_months):
    # Logic to determine avg_change value
    avg_change = 0.0
    sum_change = 0
    for i in range (1, len(inputlist)):
        sum_change+= int(inputlist[i][change_col])
    avg_change = sum_change/num_months
    return avg_change

# Function max_profit_change_at determines and returns the index at 
# which the inputlist contains max change value in the change column
def max_profit_change_at(inputlist, change_col):
    # Logic to determine maximum value and return its index
    max_index = 0
    max_change = 0
    for i in range (1, len(inputlist)):
        if  int(inputlist[i][change_col]) > max_change:
            max_change = int(inputlist[i][change_col])
            max_index = i            
    return max_index

# Function min_profit_change_at determines and returns the index at 
# which the inputlist contains min change value in the change column
def min_profit_change_at(inputlist, change_col):
    # Logic to determine minimum value and return its index
    min_index = 0
    min_change = 100000000000000
    for i in range (1, len(inputlist)):
        if  int(inputlist[i][change_col]) < min_change:
            min_change = int(inputlist[i][change_col])
            min_index = i
    return min_index



# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('Resources/budget_data.csv')

# Initialize list of records and variables
records = []
row_count = 1
total_profit = 0
profit_change = 0
previous_profit_loss = 0

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) & return csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Append the column 'Profit/Loss Change' to the header
    csv_header.append("Profit/Loss Change")
    # Append the header to the list of records
    records.append(csv_header)
    # Print the header after appending new element
    ####print(csv_header)
    
    # Read each row of data after the header
    for row in csvreader:
        # Set the 'date' and 'profit_loss' variables for better
        # readability, convert value used in calculations to int
        date = row[0]
        profit_loss = int(row[1])
        # If this is the second data row or more; calculate the change
        # using previous_change otherwise set profit_change to 0
        if (row_count>1):
            #Get the previous_profit_loss value from the records list
            previous_profit_loss = int(records[row_count-1][1])
            #Compute the change in profits (current - previous)
            profit_change = profit_loss - previous_profit_loss
        else:
            profit_change = 0                
        # Append the profit change to the row
        row.append(profit_change)
        # Append the row to the list of records
        records.append(row)
        total_profit += profit_loss
        row_count +=1
        
# Set number of month to the number of rows in records (- 1 for header)
month_count = len(records) - 1

# Call average_profit_change with records, column# for profit changes &
# period to divide by (month count -1 as first delta is 0: unavailable)
average_change_unrounded = average_profit_change(records, 2, month_count - 1)

# Round the avg change value to 2 decimal places
average_change = round(average_change_unrounded, 2)

# Call max_profit_change_at function with the list of records and 
# index for the column containing change values
max_profit_index = max_profit_change_at(records, 2)

# use max_profit_index to get corresponging month-year and profit/loss change
max_date = records[max_profit_index][0]
max_change = records[max_profit_index][2]

# Call min_profit_change_at function with the list of records and
# index for the column containing change values
min_profit_index = min_profit_change_at(records, 2)

# use min_profit_index to get corresponging month-year and profit/loss change
min_date = records[min_profit_index][0]
min_change = records[min_profit_index][2]


# Assign statements with analysis results(in required format) to a list 
line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = f"Total Months: {month_count}"
line4 = f"Total: ${total_profit}"
line5 = f"Average Change: ${round(average_change,2)}"
line6 = f"Greatest Increase in Profits: {max_date} (${max_change})"
line7 = f"Greatest Decrease in Profits: {min_date} (${min_change})"
analysis = [line1, line2, line3, line4, line5, line6, line7]

# Print financial analysis results to the terminal
for statement in analysis:
       print (statement)
        
# Set the path for the output.txt
output = Path("output.txt")

# Open the file in output path for writing "w"
with open(output, 'w') as txtfile:
# Export the analysis results line by line into the output file    
    for line in analysis:
        txtfile.write(line)
        txtfile.write('\n')
        
        
# End of Code 

# Expected Output for budget_data.csv <20th Nov 2021>
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

