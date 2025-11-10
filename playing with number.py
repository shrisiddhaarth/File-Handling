# Take input from the user
number = int(input("Enter your number: "))
             
# Store the original number for comparision later
original_number = number
reversed_number = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

# Check is the original number and the reversed number are the same
if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")



numberLargest = int(input("Enter the largest number:"))
numberSmallest = int(input("Enter your smallest number:"))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore


print("HCF is:", numberLargest)

a = int(input("Enter first number:"))
b = int(input("Enter your second number:"))

# Start with the larger number
if a < b:
    greater = a

else:
    greater = b

while True:
    if (greater % a == 0) and (greater % b ==0):
        print("LCM is:", greater)
        break
    greater += 1
