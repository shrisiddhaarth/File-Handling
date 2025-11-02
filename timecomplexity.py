def fun1(n):
    for i in range(1, 11):
        print("constant")
    return n*(n+1)/2 # Constant time complexity (1)
    
def fun2(n):
    sum = 0
    for i in range(1, n+1): #linear time complexity (n)
        sum += i
    return sum
    
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i, n+1): # n2 time complexity
            sum += i * j
    return sum
        
print(fun1(4))
print(fun2(4))
print(fun3(4))