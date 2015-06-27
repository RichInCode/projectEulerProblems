import math

def SpecialPythagoreanTriplet():
    x = [i**2 for i in xrange(1,1001)]

    #print x

    for i in xrange(0,len(x)-2):
        a = x[i]
        #print 'a = '+str(a)
        
        for j in xrange(i+1,len(x)-1):
            b = x[j]
            # print 'b = '+str(b)
            
            aAndb = a + b
            
            for k in xrange(j+1,len(x)):
                c = x[k]
                #    print 'c = '+str(c)
                #   print ' '
                    
                if aAndb == c:   # means we have a pythagorean triplet
                    aAndbAndc = a + b + c
                    #print str(a)+' '+str(b)+' = '+str(c)

                    #print 'sum = '+str( math.sqrt(a)+math.sqrt(b)+math.sqrt(c))

                    if int(math.sqrt(a)+math.sqrt(b)+math.sqrt(c)) == 1000:   # we found the special!
                        print math.sqrt(a)*math.sqrt(b)*math.sqrt(c)
                        return
                    
    print 'cannot not find it...jerk'


def main():
    SpecialPythagoreanTriplet()

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
