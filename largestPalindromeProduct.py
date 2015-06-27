def isPalindrome_string( x ):
    xstring = str(x)
    length = len(xstring)

    if length < 2:
        return False

    isPal = True

    for i in xrange(0, length/2):
        backindex = -(i+1)
        if xstring[i] != xstring[backindex]:
            isPal = False

    return isPal

def largestPalindromeProduct( numDigits ):

    largestFactor = (10**numDigits) - 1
    smallestFactor = 10**(numDigits-1)
    
    largestPossibleNumber = largestFactor**2
    smallestPossibleNumber = smallestFactor**2

    
    for x in xrange(largestPossibleNumber, smallestPossibleNumber, -1):
        if isPalindrome_string( x ):
            for i in xrange(largestFactor, smallestFactor, -1):
                if (x%i==0) and (len(str(x/i))==numDigits):
                    print x
                    return


    print 'cant find it'
            

def main():
    largestPalindromeProduct(2)
    largestPalindromeProduct(3)
    largestPalindromeProduct(4)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
