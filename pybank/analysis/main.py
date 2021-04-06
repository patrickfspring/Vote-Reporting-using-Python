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

    avgchange = totalchange / totalmonths  
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months: " + str(totalmonths))
    currency = "${:.0f}".format(nettotalamount)
    print("Total: " + currency) 
    currency2 = "${:.2f}".format(avgchange)
    #   print("Total of Changes: " + str(totalchange))
    print("Average Change: " + currency2)
    currency3 = "${:.0f}".format(greatestincrease)
    currency4 = "${:.0f}".format(greatestdecrease)
    print("Greatest Increase in Profits: " + str(date1) + " (" + currency3 + ")")
    print("Greatest Decrease in Profits: " + str(date2) + " (" + currency4 + ")")


