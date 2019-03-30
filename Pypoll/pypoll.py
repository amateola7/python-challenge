#pypoll
import os
import csv
import sys

total_votes = 0
candidates_names = ["Khan","Correy","Li","O'Tooley"]
percentage = []
khan = 0
correy = 0
li =0
otooley = 0

csvpath = os.path.join('..', 'pypoll.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    for row in csvreader:
        total_votes = (total_votes + 1)
        if "Khan" == row[2]:
            khan= khan + 1
        elif "Correy" == row[2]:
            correy = correy + 1
        elif "Li" == row[2]:
            li = li + 1
        elif "O'Tooley" ==row[2]:
            otooley = otooley + 1
    
khanprop=khan/total_votes*100
correyprop=correy/total_votes*100
liprop=li/total_votes*100
otooleyprop=otooley/total_votes*100

candidatesprop = [khanprop,correyprop,liprop,otooleyprop] 

winner = [(x,y) for x,y in zip(candidatesprop,candidates_names)]
maxwinner = [y for x,y in winner if x== max(candidatesprop)]
print("Election Results")
print("---------------------------")
print("Total Votes:  "  +str(total_votes))
print("Khan:  "  +str(round(khanprop,0))+"%"+"  " +"("+str(khan)+")")
print("Correy:  "  +str(round(correyprop,0))+"%"+"  " +"("+str(correy)+")")
print("Li:  "  +str(round(liprop,0))+"%"+"  " +"("+str(li)+")")
print("O'Tooley:  "  +str(round(otooleyprop,0))+"%"+"  " +"("+str(otooley)+")")
print("----------------------------")
print("Winner:  "  +str(maxwinner))
print("----------------------------")

sys.stdout=open('pypoll.txt','w+')
print("Election Results")
print("---------------------------")
print("Total Votes:  "  +str(total_votes))
print("Khan:  "  +str(round(khanprop,0))+"%"+"  " +"("+str(khan)+")")
print("Correy:  "  +str(round(correyprop,0))+"%"+"  " +"("+str(correy)+")")
print("Li:  "  +str(round(liprop,0))+"%"+"  " +"("+str(li)+")")
print("O'Tooley:  "  +str(round(otooleyprop,0))+"%"+"  " +"("+str(otooley)+")")
print("----------------------------")
print("Winner:  "  +str(maxwinner))
print("----------------------------")
sys.stdout.close()
sys.stdout=sys.__stdout__
 







    
            
            
            
        
        
       
   
#pypoll