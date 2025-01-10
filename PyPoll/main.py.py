# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_options = []  # Track the candidate names
candidate_votes = {}  # Dictionary to track vote counts

# Winning Candidate and Winning Count Tracker
winning_candidate = ""  # Track the winning candidate
winning_count = 0  # Track the winning vote count
winning_percentage = 0 # Track the winning vote percentage

# Open the CSV file and process it
with open(file_to_load) as election_data: # Open the data file
    reader = csv.reader(election_data) # Read the data file

    # Skip the header row
    header = next(reader) # Skip the header row

    # Loop through each row of the dataset and process it
    for row in reader: # Loop through each row of the dataset

        # Print a loading indicator (for large datasets)
        # print(". ", end="") # Print a loading indicator (for large datasets)

        # Increment the total vote count for each row
        total_votes += 1 # Increment the total vote count for each row

        # Get the candidate's name from the row
        candidate_name = row[2] # Get the candidate's name from the row

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options: # If the candidate is not already in the candidate list, add them
            candidate_options.append(candidate_name) # Add the candidate to the candidate list

            # Start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0 # Start tracking the candidate's vote count

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1 # Add a vote to the candidate's count

# Open a text file to save the output
with open(file_to_output, "w") as txt_file: # Open a text file to save the output

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n") # Print the total vote count (to terminal)
    print(election_results, end="") # Print the total vote count (to terminal)

    # Write the total vote count to the text file
    txt_file.write(election_results) # Write the total vote count to the text file



    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes: # Loop through the candidates to determine vote percentages and identify the winner
        votes = candidate_votes[candidate] # Get the vote count for the candidate
        vote_percentage = float(votes) / float(total_votes) * 100


        # Get the vote count and calculate the percentage
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes})\n") # Get the vote count and calculate the percentage

        # Update the winning candidate if this one has more votes
        if (votes > winning_count): # Update the winning candidate if this one has more votes
            winning_count = votes
            winning_candidate = candidate

        # Update the winning candidate if this one has more votes and higher percentage

        # Print and save each candidate's vote count and percentage
        print(candidate_results, end="") # Print and save each candidate's vote count and percentage
        txt_file.write
    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n") # Generate and print the winning candidate summary
    print(winning_candidate_summary) # Generate and print the winning candidate summary

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary) # Save the winning candidate summary to the text file