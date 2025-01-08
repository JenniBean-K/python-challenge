# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv # Import the csv module
import os # Used for file path manipulation (os.path.join)

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:/path/to/your/Resource/budget_datacsv")  # Input file path. Should contain your financial data.
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path. Will store the analysis results.

# Define variables to track the financial data
total_months = 0 # Tracks the total number of months included in the dataset
total_net = 0 # Tracks the net total amount of "Profit/Losses" over the entire period

# Add more variables to track other necessary financial data
previos_net = 0 # Tracks the previous month's profit/loss for calculating changes
changes = [] # Tracks the monthly changes in profit/loss between months
greatest_increase = ["", 0] #Tracks the the amount of the greatest increase in profit
greatest_decrease = ["", 0] #Tracks the the amount of the greatest decrease in profits

# Open and read the csv
with open(file_to_load) as budget_data: # Open the file
    reader = csv.reader(budget_data) # Read the file

    # Skip the header row
    header = next(reader) # Skip the header row

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader) # Extract the first row to avoid appending to net_change_list
    total_months += 1 # Track the total number of months
    total_net += int(first_row[1]) # Track the total net change
    previous_net = int(first_row[1]) # Track the previous net change

    # Track the total and net change
    for row in reader: # Process each row of data
        date = row[0] # Extract the date from the row
        net = int(row[1]) # Extract the profit/loss from the row

    # Process each row of data
    for row in reader: # Process each row of data
        date = row[0] # Extract the date from the row
        net = int(row[1]) # Extract the profit/loss from the row

        # Track the total
        total_months += 1 # Track the total number of months
        total_net += net # Track the total net change

        # Track the net change
        net_change = net - previous_net # Calculate the net change
        previous_net = net # Track the previous net change
        changes.append(net_change) # Append the net change to the changes list

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]: # Check if the net change is greater than the current greatest increase
            greatest_increase[date, net_change] # Update the greatest increase


        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]: # Check if the net change is less than the current greatest decrease
            greatest_decrease[date, net_change] # Update the greatest decrease


# Calculate the average net change across the months
average_change = sum(changes) / len(changes) # Calculate the average net change

# Generate the output summary
output = ( 

)

# Print the output
print(output) # Print the output

# Write the results to a text file
with open(file_to_output, "w") as txt_file: # Open the file
    txt_file.write(output) # Write the output to the file
