height = 68 # inches
if height > 70 :
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")


name = ""
list_a = []

if list_a:
    print("I will not run")
else:
        print("I am Empty")


numbers = [1,2,3,4,5]

for number in numbers:
    print(number)


for i in range(0,7):
    print("I would love " + str(i) + " cookies")



players = 11

while players >= 5 :
    print("The remaining players are",players)
    players -= 1




number = 0
while True:
    print("I love candy "+ str(number))
    number +=1
    if number == 7 :
        break   



# taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

# loop
for i in range(1,15):
    if i in numTaken:
        continue
    print(i)