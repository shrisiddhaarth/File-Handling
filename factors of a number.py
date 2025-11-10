num = int(input("enter a number"))

print(f"Factors of {num } are:" , end="")
for i in range(2, num + 1):
    if num % i ==0:
        print(i, end=",")
