"""
Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.
"""
import json
import os
filename = "data.txt"
def start():
    if os.path.isfile(filename) == False:
        file = open(filename,"w")
        file.write('["SubjectA","GradeA","SubjectB","GradeB","SubjectC","GradeC","SubjectD","GradeD"]')
    else:
        fileRead = open(filename,"r")
        inputdata = fileRead.read()
        global list1
        list1 = json.loads(inputdata)

def firstFunc():
    x = input("Enter the subject you want to change: ")
    y = input("Enter what you want to change it to: ")
    if x in list1:
        list1.replace(x,y)
        print(list1)

start()
firstFunc()