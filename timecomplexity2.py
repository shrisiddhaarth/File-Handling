def printnumber(n):
    itertation = 0
    for i in range(1, 10):
        print(i, "hello world")
        print("the total number entered by the user is " ,n)
    itertation += 1
    print("the total iteration done by computer is",itertation"\n")

printnumber(10)
printnumber(200)
print("\n with any 'n' the time taken by the computer will not change")

def Ontime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
        print("When n is" ,n,"Iterations =" ,iteration)
Ontime(10)
Ontime(20)
Ontime(42)

print("\nWith every 'n' the time takena and iterations taken will increase linearly")
