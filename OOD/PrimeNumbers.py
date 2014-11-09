__author__ = 'Pat'
import sys

## Method that determines if a number is prime
def isPrime(max):
    for x in range (2, max):
        if(max % x == 0):
            return 0
    return 1

while(1):
    print('Enter 0 to quit')
    number = int(input('Please enter a number: '))

    if(number == 0):
        sys.exit('')

    for num in range(2, number):
        if(isPrime(num) == 1):
            print(int(num))

