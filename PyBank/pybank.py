#pybank
import os
import csv
import sys

month = []
profit_losses = []
profit_losses_future = []
newmonth = []
newmonth_change=[]

csvpath = os.path.join('..', 'pybank.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    for row in csvreader:
        month.append(row[0])
        profit_losses.append(int(row[1]))
        profit_losses_future.append(int(row[1]))
        newmonth.append(row[0])
        
    total=sum(profit_losses)
    del(profit_losses_future [0])
    del(profit_losses [len(month)-1])
    del(newmonth[0])
    change=[x- y for x,y in zip(profit_losses_future,profit_losses)]
    changesum = sum(change)
    
    newmonth_change = [(x,y) for x,y in zip(newmonth,change)]
    maxmonth = [x for x,y in newmonth_change if y==max(change)]
    minmonth = [x for x,y in newmonth_change if y==min(change)]


print("Financial Analysis")
print("------------------------")
print ("Total Months: "+str(len(month)))
print("Total: $"+str(total))
print("Average Change: $"+ str(round(changesum/(len(month)-1),2)))
print("Greatest Increase in Profits: " + str(maxmonth) +"  $"+ str(max(change)))
print("Greatest Decrease in Profits: " + str(minmonth) +"  $"+ str(min(change)))
sys.stdout=open('pybank.txt','w+')                                        
print("Financial Analysis")
print("------------------------")
print ("Total Months: "+str(len(month)))
print("Total: $"+str(total))
print("Average Change: $"+ str(round(changesum/(len(month)-1),2)))
print("Greatest Increase in Profits: " + str(maxmonth) +"  $"+ str(max(change)))
print("Greatest Decrease in Profits: " + str(minmonth) +"  $"+ str(min(change)))
sys.stdout.close()
sys.stdout=sys.__stdout__