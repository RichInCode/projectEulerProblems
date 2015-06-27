import math

def isPrime( x , low = 3):
    
    prime = True

    num=x
    #num = x/2
    num = math.sqrt(x)    
    i = low

    while i < num+1:
        if x%i==0:
            prime = False
        i = i+2;

    return prime


def largestPrimeFactor( x ):

    num = x/2
    i = 3

    while i < num:
        if x%i==0:
            #print i
            if isPrime( i ):
                #print i
                largestPrime = i
                num = x/i;
        i = i+2

    print largestPrime

def main():
    largestPrimeFactor(13195)
    largestPrimeFactor(600851475143)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
