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

    # Format the Print statements for terminal and then write to output file 

    print("Election Results")
    print("----------------------------") 
    print("Total Votes: " + str(totalnumbervotes))
    print("----------------------------")

    text_file = open("myoutput.txt", "w")
    print(f"Election Results", file=text_file)
    print(f"----------------------------", file=text_file) 
    print(f"Total Votes: " + str(totalnumbervotes), file=text_file)
    print(f"----------------------------", file=text_file)

    # Loop through candidate results and print/write detail lines

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
        print(candidatename + ": " + formatpercent + " (" + str(candidatevotes) + ")", file=text_file)

    print("----------------------------")
    print("Winner: " + winning_candidate)
    print("----------------------------")
    
    # Close out the text file with final print statements

    print(f"----------------------------", file=text_file)
    print(f"Winner: " + winning_candidate, file=text_file)
    print(f"----------------------------", file=text_file)
    text_file.close()
