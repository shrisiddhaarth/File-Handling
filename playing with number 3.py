# Solution 2
from math import sqrt
n = int(input("Enter a number to check if it is prime : "))
if n > 1:
    for i in range (2, int(sqrt(n))+1):
        if n % i == 0:
            print ("The number is not prime")
            break
    else:
         print("The number is prime")
else:
    print("The number is smaller than 2")
