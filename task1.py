"""
Have the user enter in their name and email address.
Have the program create a file called 'task1.txt'
Write their name to the first line and their email to the second line.

Example:
What is your name? Joe Lunchbox
What is your email? joe@sandwiches.org 

task1.txt contents:
Joe Lunchbox
joe@sandwiches.org 
"""

filename = 'task1.txt'
file = open(filename, 'w')
data1 = input("What is your name? ")
data2 = input("What is your email? ")
file.write(f"{data1}\n{data2}")
file.close()