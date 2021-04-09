import os
import csv

# Path to collect data from the Resources folder
budgetdata_csv = os.path.join('..', 'resources', 'budget_data.csv')

# Read in the CSV file
with open(budgetdata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    totalmonths = 0
    prevamount = 0
    totalchange = 0
    nettotalamount = 0
    greatestincrease = 0
    greatestdecrease = 0

    # Loop through the data

    for row in csvreader:

        totalmonths = totalmonths + 1
        nettotalamount = nettotalamount + int(row[1])
      
        if prevamount != 0:
            rowchange = int(row[1]) - prevamount

            totalchange = totalchange + rowchange
            if rowchange > greatestincrease:
                date1 = row[0]
                greatestincrease = rowchange

            if rowchange < greatestdecrease:
                date2 = row[0]
                greatestdecrease = rowchange   

        prevamount = int(row[1])

    # Divide by number of changes, not months in the file

    avgchange = totalchange / (totalmonths - 1)  
    
    # Format and print to terminal
    
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months: " + str(totalmonths))
    currency = "${:.0f}".format(nettotalamount)
    print("Total: " + currency) 
    currency2 = "${:.2f}".format(avgchange)
    
    print("Average Change: " + currency2)
    currency3 = "${:.0f}".format(greatestincrease)
    currency4 = "${:.0f}".format(greatestdecrease)
    print("Greatest Increase in Profits: " + str(date1) + " (" + currency3 + ")")
    print("Greatest Decrease in Profits: " + str(date2) + " (" + currency4 + ")")
    
    # Export the output to a txt file 
    
    with open("myoutput.txt", "w") as text_file:
        print(f"Financial Analysis", file=text_file)
        print(f"----------------------------", file=text_file) 
        print(f"Total Months: " + str(totalmonths), file=text_file)
        print(f"Total: " + currency, file=text_file) 
        print(f"Average Change: " + currency2, file=text_file )
        print(f"Greatest Increase in Profits: " + str(date1) + " (" + currency3 + ")", file=text_file)
        print(f"Greatest Decrease in Profits: " + str(date2) + " (" + currency4 + ")", file=text_file)
        text_file.close()