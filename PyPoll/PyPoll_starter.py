# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

#s to load and output (update with correct file paths)
file_to_load = os.path.join(".","Resources","election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
vote_dict = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter = ",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            vote_dict[candidate_name] = 0

        # Add a vote to the candidate's count
        vote_dict[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote output (to terminal)
    vote_output = (f'Election Results\n'
                   f'-------------------------\n'
                   f'Total Votes: {total_votes}\n'
                   f'-------------------------\n'
                   )
    print(vote_output)

    # Write the total vote count to the text file
    txt_file.write(vote_output)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:
    
        # Get the vote count and calculate the percentage
        votes = vote_dict[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        
        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes 
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_vote_total = f'{candidate}: {vote_percentage: .3f}%: ({votes})\n'
        print(candidate_vote_total)
        txt_file.write(candidate_vote_total)

    # Generate and print the winning candidate summary
    winner_output = (f'-------------------------\n'
                      f'Winner: {winning_candidate}\n'
                      f'-------------------------\n')
    print(winner_output)
    # Save the winning candidate summary to the text file
    txt_file.write(winner_output)