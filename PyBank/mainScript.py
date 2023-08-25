import os
import csv

# Clear terminal function for easy viewing
def clearScreen():
    print("\033[2J")
    print("\033[H")

#Create the path 
pyBank_csvPath = os.path.join(".", "Resources", "budget_data.csv")
outputFile = os.path.join(".", "budget_analysis.txt")

totalMonths = 0
totalNet = 0
netChange_list = []

greatest = ["", 0]
least = ["", 999999999999999]


# Open and read CSV
with open(pyBank_csvPath, 'r') as financialData:
    csvReader = csv.reader(financialData, delimiter=',')

    # Read the header row
    csvHeader = (next(csvReader))
    #print(f"Header {csvHeader}")

    firstRow = next(csvReader)
    
    totalNet += (int(firstRow[1]))

    previousNet = (int(firstRow[1]))
    
    totalMonths += 1

    for row in csvReader:
        totalMonths += 1
        totalNet += int(row[1])
        
        # Track the net change 
        netChange = int(row[1]) - previousNet
        previousNet = int(row[1])
        netChange_list.append(netChange)

        #calculate the greatest increase
        if(netChange > greatest[1]):
            greatest[0] = row[0]
            greatest[1] = netChange

        #calculate the greatest decrease 
        if (netChange < least[1]):
            least[0] = row[0]
            least[1] = netChange

        
        # calculate the greatest decrease 
#print(netChange_list)
#print(greatest)
#print(least)
netMonthlyAverage = sum(netChange_list)/ len(netChange_list)

output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total months: {totalMonths}\n"
    f"Total:  ${totalNet}\n"
    f"Average change: ${netMonthlyAverage:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in profits: {least[0]} (${least[1]})\n"
)

print(output)

with open(outputFile, "w") as txt_file:
      txt_file.write(output)

    

    
