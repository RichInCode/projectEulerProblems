import largestPrimeFactor

def nthPrime( x ):
    
    index = 3

    x = x-2  # automatically count 2 and 3

    while x > 0:
        index = index + 2
        if largestPrimeFactor.isPrime(index):
            prime = index
            #print prime
            x = x-1
            
    

    print prime

def main():
    nthPrime( 6 )
    nthPrime( 10001 )


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
