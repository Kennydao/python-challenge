# define function to print out the results
def publish_result():
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {len(budget)}')
    print(f'Total: ${Ttl}')
    print(f'Average Change: ${Ttl/len(budget):.2f}')
    print(f'Greatest Increase in Profits: {budget[0][1]} (${budget[0][0]})')
    print(f'Greatest Decrease in Profits: {budget[-1][1]} (${budget[-1][0]})\n')
    return
# main script to analyze records in budget_data.csv file
import csv
import os
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
csvf = open(csvpath)
# define budget variable as list
budget = list()
# reading the csvfile
reader = csv.reader(csvf, delimiter=',')
# set the file pointer to the 1st row
next(csvf,None)
Ttl = 0 # to store total budget amount
# creating a list of budget includes month and amount, storing the total amount of budget
for row in reader:
    c1 = str(row[0])
    c2 = int(row[1])
    item = c2,c1
    budget.append(item)
    Ttl = Ttl + c2
# sorting the budget list largest to smallest to indetify greatest increase/decrease
budget = sorted(budget, reverse=True)
# closing file after usage
csvf.close()
# call function to print out result to terminal screen
publish_result()
# to output result into text file
import sys
txtpath = os.path.join("Resources","analysis.txt")
f = open(txtpath, "w")
sys.stdout = f
publish_result()
# closing file once task done
f.close()