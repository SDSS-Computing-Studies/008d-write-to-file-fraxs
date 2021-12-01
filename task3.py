#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
import json
filename = "task3.txt"
file = open(filename, 'w')


def func():
    x = input("Enter a word: ")
    return x
a = func()
b = func()
c = func()
d = func()
e = func()
list1 = [a,b,c,d,e]
outputData = json.dumps(list1)
print(outputData)
print(list1)
file.write(outputData)
file.close()