#PyBank
# Import Budget Data
import csv
# not using path since csv file is in the same folder
# Open budget_data.csv as variable 
with open ("budget_data.csv", 'r', newline='') as infile:
#Reading the csv file 
    reader = csv.DictReader(infile)

    count = 0
    month = []

    for row in reader: 
        count = count + 1
    #print(row["Date"])
    #month.append(row['Date'])
        #print(row["Profit/Losses"])
        month.append(float(row['Profit/Losses']))



print("Total Months: ", len(month))
print("Total: ", sum(month))
print("Average Change: ", sum(month)/len(month))



















   


























     



























  



       





        
    








