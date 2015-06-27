def smallestMultiple( uplimit ):

    number = uplimit
    allGood = True

    while 1:
        allGood = True
        for i in xrange(1, uplimit+1):
            if number%i != 0:
                allGood = False
                break
        if allGood == True:
            print number
            break
        else:
            number = number + 1


def main():

    smallestMultiple( 10 )
    smallestMultiple( 20 )
    #smallestMultiple( 30 )


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
