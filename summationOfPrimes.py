import largestPrimeFactor
import math

def summationOfPrimes( x ):
    
    runningSum = 2
    lastPrime = 3
    i = 3

    while i < x:
        
        if largestPrimeFactor.isPrime( i ):
            runningSum = runningSum + i
            lastPrime = i
            print i

        i = i+2


    print runningSum

def main():
    #summationOfPrimes( 10 )
    summationOfPrimes( 2000000 )


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
