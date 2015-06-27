def fibonacci( x ):
    a = 1
    b = 1
    fib = 1

    runningSum = 0

    print fib
    for i in range(x):
        fib = a + b
        if fib > 4000000:
            break

        if fib%2 == 0:
            runningSum = runningSum + fib

        a = b
        b = fib
        print fib

    print 'sum = '+str(runningSum)


def main():
    fibonacci( 4000000 )


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
