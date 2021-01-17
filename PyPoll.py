import csv
import os

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#Create a filename variable to save election analysis work
file_to_save = 'Analysis/election_analysis.txt'

#Open the election results and read the file    
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and print header rows
    headers = next(file_reader)
    print(headers)

#1. Total # of votes cast

#2. Complete list of candidates who recieved votes

#3. Total # of votes each candidate recieved

#4. % of votes each candidate won

#5. Winner of election based on popular vote
