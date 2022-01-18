"""
When the program loads, check to see if the file problem1.txt exists. If it does, see if the data can be interpreted using json.  
"""
import json
import os
if os.path.exists("problem1.txt"):
    filename = 'problem1.txt'
    file = open(filename, 'r')
    if os.stat(filename).st_size == 0:
        print("The file is empty")
    else:
        outputData = json.loads(file)
        
else:
    print("The file does not exist")