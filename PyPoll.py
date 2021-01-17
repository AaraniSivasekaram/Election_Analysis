import csv
import os

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#Create a filename variable to save election analysis work
file_to_save = 'Analysis/election_analysis.txt'

#Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

#Define dictionary
candidate_votes = {}
candidate_votes = {"Charles Casper Stockham": total_votes, "Diana DeGette": total_votes, "Raymon Anthony Doane":total_votes}

#Detemining winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file    
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read and print header rows
    headers = next(file_reader)

    #For each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        
        #2. Complete list of candidates who recieved votes
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking a candidate's votes
            candidate_votes[candidate_name] = 0
       
       #3. Total # of votes each candidate recieved
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1 

#4. % of votes each candidate won
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100 
    print(f"{candidate_name} , {total_votes:,} votes, {vote_percentage:.1f}%")

    #5. Winner of election based on popular vote
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

#Print the winning candidate's results 
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote Count:{winning_count:,}\n"
    f"Winning Percentage:{winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)
    
