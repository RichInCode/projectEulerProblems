import csv

def LargestProductInAGrid():
    my_matrix = [[0 for x in xrange(20)] for x in xrange(20)]

    with open ( 'data.txt', 'rb') as csvfile:
        l = csv.reader(csvfile, delimiter=' ')

        largestProduct = 0

        i = 0
        for row in l:
            my_matrix[row][i] = row
            #print ' '.join(row)
            
        print my_matrix


def main():
    LargestProductInAGrid()


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
