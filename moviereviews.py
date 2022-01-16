# Reading csv file 
import csv
with open('userReviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
    csv_reader = csv.reader(userreviews, delimiter=';')
    next(csv_reader, None)
    
#Declaring variables
    author = []
    moviename = []
    score = []
    reviewerlist = []
    personal_score = 9.0
    moviename = 'lawless'
    
    count = 0
    sum = 0
    avg = 0
    
#calculating sum and avg 
    for i in csv_reader:
        if (i[0]) == 'lawless':
            sum+=float(i[1])
            count = count+1
            reviewerlist.append(i[2])
            print(reviewerlist)
            print("Scores- " + (i[1]))
            print("Sum - " + str(sum))
            print("Count - " + str(count))
            
    avg = sum/count
    print(avg)
            

avg = sum/count
print ("Avg score - " + moviename + " : " + str(avg))
print ("Compariing - " + str(personal_score-avg) + " (The differemce is 2.7333333333333334  between personal  reviews' score.)")

#lawles reviews list 
print(moviename + " reviewers list: ")
print(reviewerlist)




#print out the final outputs. 
with open('userReviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
  filelist = []
  Finallist = []
  csv_reader = csv.reader(userreviews, delimiter=';')
  
# list of of reviewers, scores and movienames 
  for i in csv_reader:
        if(i[2]) in reviewerlist and float(i[1]) > float(avg):
            print('Reviewer: ' + i[2] + " Score: " + str(i[1]) +' Moviename: ' + str(i[0]))
            filelist.extend([i[0], i[1], i[2]])
            Finallist.extend([filelist])
            print(filelist)
            filelist = []



## Printing out author, moviename and userscore into a  csv file list based on the output. 
fields = [['Moviename' , 'Userscore','Author' ]] 
file = open('Finaloutput.csv', 'w+', newline = '')
with file:
    write = csv.writer(file)
    write.writerow(fields)
    write.writerows(Finallist)