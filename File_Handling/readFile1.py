from typing import Counter


handle = open("test.txt", "r")
data = handle.read()
counter = 0
for word in data.split():
    if word == "Python":
        counter +=1
print (counter)