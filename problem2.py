"""
Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.
"""
import json
import os
import time as t
filename = "data.txt"
def start():
    if os.path.isfile(filename) == False:
        file = open(filename,"w")
        file.write('["SubjectA","GradeA","SubjectB","GradeB","SubjectC","GradeC","SubjectD","GradeD","SubjectE","GradeE","SubjectF","GradeF","SubjectG","GradeG","SubjectH","GradeH"]')
    else:
        fileRead = open(filename,"r")
        inputdata = fileRead.read()
        global list1
        list1 = json.loads(inputdata)

def firstFunc():
    x = input("Enter the subject you want to change: ")
    y = input("Enter what you want to change it to: ")
    for i in range(len(list1)):
        if x in list1[i]:
            list1[i] = y

def secondFunc():
    x = input("Enter the subject you want to change the grade of: ")
    y = input("Enter what you want to change the grade to: ")
    for i in range(len(list1)):
        if x in list1[i]:
            list1[i+1] = y

def thirdFunc():
    print(f" SUBJECT:GRADES \n{list1[0],list1[1]}\n{list1[2],list1[3]}\n{list1[4],list1[5]}\n{list1[6],list1[7]}\n{list1[8],list1[9]}\n{list1[10],list1[11]}\n{list1[12],list1[13]}\n{list1[14],list1[15]}")
    t.sleep(5)
def fourthFunc():
    x = json.dumps(list1)
    fileWrite = open(filename,"w")
    fileWrite.write(x)
    print("File saved!")

def close():
    exit()


def main():
    start()
    while True:
        x = input("1. Change the name of a subject \n2. Change the grade for a subject \n3. Read subject data \n4. Save the current data \n5. Exit the program \n")
        if x == '1':
            firstFunc()
        elif x == '2':
            secondFunc()
        elif x == '3':
            thirdFunc()
        elif x == '4':
            fourthFunc()
        elif x == '5':
            close()
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()