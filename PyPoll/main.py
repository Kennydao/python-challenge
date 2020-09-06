# This function is to publish the election results
def publish_result():
    print('---------------------------')
    print('Total Votes: ',total_votes)
    print('---------------------------')
    # loop through the list to print out candidate name and his/her respective polls
    for candi in candi_lst:
        print(f'{candi[1]} : {candi[0]/total_votes:.3%} ({candi[0]})')
    # print out the winner, who is the first element in the sorted candi_lst
    print('---------------------------')
    print(f'Winner: {candi_lst[0][1]}')
    print('---------------------------')
    return
# main script for counting polls
import os
import csv
# define variables
vote = dict() # records of candidates name and polls
candi_lst = list() # list of candidate to sort out the winner, polls calculation
total_votes = 0 # to store total number of polls
# Set path for csv file and open file
csvpath = os.path.join("Resources", "election_data.csv")
csvfile = open(csvpath)
csvreader = csv.reader(csvfile, delimiter=",")
next(csvfile, None) # set the file pointer to 1st row
# creating a dictionary to record candidates name and polls
counter = 0 # to displaying number while making users waiting
for row in csvreader:
    vote[row[2]] = vote.get(row[2],0) + 1 # adding name and counting polls for candidate
    counter +=1
    # displaying polls counting status on screen while user waiting
    if counter%100 ==0:
        print('Counting polls: ', counter, end='\r')
# creating a candidate list, and storing the total of votes
for k,v in vote.items():
    newcandi = (v,k)
    total_votes = total_votes + v
    candi_lst.append(newcandi)
# sorting candidate by number of votes (largest to smallest) to pick out the winner
candi_lst = sorted(candi_lst, reverse=True)
# closing file after usage
csvfile.close()
# print election results to terminal screen
publish_result()
# output election results to text file
import sys
txtpath = os.path.join("Resources","election_result.txt")
f = open(txtpath, "w")
sys.stdout = f
publish_result()
f.close()