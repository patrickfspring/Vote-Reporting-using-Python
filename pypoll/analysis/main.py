import os
import csv

candidates = {}

# Path to collect data from the Resources folder
electiondata_csv = os.path.join('..', 'resources', 'election_data.csv')

# Read in the CSV file
with open(electiondata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    totalnumbervotes = 0

    # Loop through the data
    for row in csvreader:
        totalnumbervotes = totalnumbervotes + 1

        if row[2] not in candidates:
            candidates[row[2]] = 0
        
        candidates[row[2]] +=1

    print("Election Results")
    print("----------------------------") 
    print("Total Votes: " + str(totalnumbervotes))
    print("----------------------------")

    winning_sofar = 0
    for x, y in candidates.items():
        candidatename = x
        candidatevotes = y
        if candidatevotes > winning_sofar:
            winning_sofar = candidatevotes
            winning_candidate = candidatename 
        percentvotes = ((candidatevotes / totalnumbervotes ) * 100)
        formatpercent = "{:.3f}%".format(percentvotes)
        print(candidatename + ": " + formatpercent + " (" + str(candidatevotes) + ")")

    print("----------------------------")
    print("Winner: " + winning_candidate)
    print("----------------------------")
    print(candidates)
