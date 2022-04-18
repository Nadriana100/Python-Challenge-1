#PyPoll
# Import Election Data
import csv
# Open election_data.csv as variable 
with open ("election_data.csv", 'r', newline='') as infile:
  
#Reading the csv file 
    reader = csv.reader(infile)
    #print(reader)


    firstrow= next(reader)  # skip headers 
    count = 1
    totalNumVotes = 0
    candidates = {}
    votes_winers_percg = []
    winner = []
  
    #print(firstrow)

    for row in reader:
      if row[2] not in candidates.keys():
        candidates[row[2]] = 1
   # print(candidates)
      else: 
        candidates[row[2]] += 1 
    #print(candidates)
      totalNumVotes += 1
    

        #dict.items()
        #dict.values() -> values
# print(candidates.items()) List Candidate's names and num of votes.

""""
RESULTS= main.py

print("----------------------")
print("Total Votes:", totalNumVotes)
print("----------------------")
for candidate, vote in candidates.items():
  print(f"{candidate}: {round(vote/totalNumVotes * 100,3)} %  ({vote}) "  )
print("----------------------")
print(f"Winner: {max(candidates, key=candidates.get)}")

Total Votes: 3521001
----------------------
Khan: 63.0 %  (2218231)
Correy: 20.0 %  (704200)
Li: 14.0 %  (492940)
O'Tooley: 3.0 %  (105630)
----------------------
Winner: Khan
"""

# EXPORTING TO A TEXT FILE myfile.txt

file = open("myfile.txt","w")
file.write("----------------------\n")
file.write(f"Total Votes: {totalNumVotes} \n" )
file.write("----------------------\n")
for candidate, vote in candidates.items():
  file.write(f"{candidate}: {round(vote/totalNumVotes * 100,3)} %  ({vote}) \n" )
file.write("----------------------\n")
file.write(f"Winner: {max(candidates, key=candidates.get)} \n")
file.close()
  
