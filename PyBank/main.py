#PyBank
# Import Budget Data
import csv
# Open budget_data.csv as variable 
with open ("PyBank/budget_data.csv", 'r', newline='') as infile:
  
#Reading the csv file 
    reader = csv.reader(infile)
    next(reader)  # skip headers 
    count = 1
    month = []
    avg = []
    date = []

    firstrow = next(reader) # 1st line
    month.append(float(firstrow[1]))  # saving lost and profit 1st line 
    date.append(firstrow[0])
    avg.append(0)

    for row in reader: 
        count = count + 1
        month.append(float(row[1]))
        avg.append(float(row[1]) -float(month[count -2]))
        date.append(row[0])

        greatinc = max(avg)
        greatdec = min(avg)

print("Total Months: ", len(month))
print("Total: ", sum(month))
print("Average Change: ", sum(avg)/len(avg))
print("Geatest Increast in Profits: ", date[avg.index(greatinc)],  greatinc)
print("Geatest Decreast in Profits: ", date[avg.index(greatdec)], greatdec)

