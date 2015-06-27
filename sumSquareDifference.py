def sumSquareDifference( x ):
    
    sumOfSquares = 0
    squareOfSums = 0

    for i in xrange(1,x+1):
        sumOfSquares = sumOfSquares + i**2
        squareOfSums = squareOfSums + i


    squareOfSums = squareOfSums**2

    print squareOfSums - sumOfSquares

def main():
    sumSquareDifference( 10 )
    sumSquareDifference( 100 )

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
