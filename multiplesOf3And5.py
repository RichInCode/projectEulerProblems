def  multiplesOf3and5( x ):
    
    bigSum = 0

    for i in range(x):
        if (i%3==0) or (i%5==0):
            bigSum = bigSum + i

    print bigSum

def main():
    multiplesOf3and5( 1000 )

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
