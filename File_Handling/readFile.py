handle = open("test.txt", "r")  #open the file

data = handle.read() #reading the whole file
data =  handle.readline() #it will read a single line
data = handle.readlines() #It will read multiple lines
print(data)

handle.close  #close the file, saves on memory and eradicates errors from the application