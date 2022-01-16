import math
from pprint import pprint
import argparse, sys

# Initializing the class for Fermat
class nMiss:
	def __init__(self, a,b,c,miss):
		self.a = a
		self.b = b 
		self.c = c
		self.miss = miss 

# Initializing the class for Rieman
class Rieman:
	def __init__(self, n, n_zeros, firsthalf, secondhalf):
		self.n = n 
		self.number_of_zeros = n_zeros 
		self.first_half = firsthalf
		self.second_half = secondhalf

# Calculates Fermat near-misses for a given range for the base and given n
def getFermatMiss(a,b,c, n):
    d = (math.pow(c, n) - math.pow(a, n) - math.pow(b, n))
    nr = (n*math.pow(c, n-3))
    if d == 0:
        d = 1
    nm = round(nr/d, 1)
    #Outputting the Fermat results
    return nMiss(a,b,c,nm).__dict__


# Calculates the Riemann-Zeta zeroes
def riemann(n):
    n_zeros = str(2*(n +1))
    print(f"For {str(n)} we have {n_zeros} zeros")
    firsthalf = [] 
    secondhalf = []    

    x = list(range(0,n + 1))
    theta = math.pi/3
    for i in x:
        y = (math.pi/3)*(1+6*i)
        y = math.sqrt((y**2/theta**2)-0.25)
        #The first half of zeros added to the array
        firsthalf.append({i : y}) 
        z = (5*math.pi/3)*(1+6/5*i)
        z = math.sqrt((z**2/theta**2)-0.25)
        #The second half of zeros added to the array
        secondhalf.append({i : z}) 

    #Outputting the Rieman results
    return Rieman(n, n_zeros, firsthalf, secondhalf).__dict__

# The main function
def main():
    parser = argparse.ArgumentParser(description="Calculater Fermat near-misses and Riemann-Zeta zeroes.")
    parser.add_argument("-f", "--fermat", help="Calculate Fermat near-misses", action='store_true')
    parser.add_argument("-r", "--rieman", help="Calculate Riemann-Zeta zeroes", action="store_true")
    parser.add_argument("-n", help = "value of n")


    
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    if not args.n:
        n = int(input("Please enter value for n(>2) :"))
    else:
        try:
            n = int(args.n)
        except ValueError:
            print(f"[!]Please re-run with a valid value of n")
            sys.exit(1)





    if n < 2:
        print(f"[!]Value of n should be > 2")
        sys.exit(1)

    # Taking the user input for fermat
    if args.fermat:
        print(f"\n\tFermat near-misses when start n = {n}")
        a = int(input("Enter a (a > 0)      : "))
        b = int(input("Enter b (b >= a)     : "))
        c = int(input("Enter c (b < c < 2^23 ) : "))
        if not 0 < a <= b < c < 2**23:
            print("Enter valid range a,b or c")
            sys.exit(1) 
        pprint(getFermatMiss(a, b,c, n))
    
    # Taking the user input for rieman
    if args.rieman:
        print(f"\n\tRiemann-Zeta zeroes when n = {n}")
        pprint(riemann(n))
        print("\n")


# Executing the program
if __name__ == "__main__":
    main()


#On the terminal run python3 problem5.py -f for fermat solution or python3 problem5.py -r for reiman to run and compile
#Enter the input values asked as you click enter