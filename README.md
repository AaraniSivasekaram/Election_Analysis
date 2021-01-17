# Election_Analysis

## Election Audit Overview
The Colorado Board of Elections outlined several tasks to analyze the election results, including determining the winner of recent congressional election and determining the county with the largest voter turnout. The auditing tasks included:

1. Calculating the total number of votes
2. Identifying a complete list of candidates who recieved votes
3. Calculating the number of votes and percentage of votes per county
4. Determining the county with the largest voter turnout
5. Calculating the total number of votes each candidate recieved
6. Calculating the percentage of votes each candidate won
7. Determining the winner of the election based on the popular vote

## Project Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.52.1

## Election Audit Results Summary
The analysis of the election results indicated below are also reflected in the election_analysis.txt file (https://github.com/AaraniSivasekaram/Election_Analysis/blob/main/election_analysis.txt)

- There were 369,711 total votes cast in the election
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The proportion and number of votes stratified by county were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- The county with the largest voter turnout was:
  - Denver 
- The candidate results were:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the total votes cast which equalled 272,892 votes. 

## Election Audit Summary
The great thing about this script is that it can be modified and used for other State and County elections, given a few limitations. 
- If a State or County tabulates votes in the exact same format, we can upload and read through different files in Python by modifying line 9 (https://github.com/AaraniSivasekaram/Election_Analysis/blob/main/File_to_load%20image.png) to include the appropriate path to a new file_to_load and run this analysis across a different .csv file.
- If a State or County tabulates their votes in a .csv file but uses different orders of values or extra values, we can modify the row identification lines to retrieve appropriate values including: candidate name, county name, vote counts and etc. Here is an screenshot of a row indentification line that we can modify to retrieve the correct information from a different .csv file (https://github.com/AaraniSivasekaram/Election_Analysis/blob/main/Row_indentification%20image.png). 
