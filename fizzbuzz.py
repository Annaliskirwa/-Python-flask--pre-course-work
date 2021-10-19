def fizzbuzz(int):
    for i in range (0,100):
        if i%3 == 0:
            print("fizz")

        if i%5 == 0:
            print ("buzz")

        if i%15 == 0:
            print("fizzbuzz")
    return (fizzbuzz)
#this one runs
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)