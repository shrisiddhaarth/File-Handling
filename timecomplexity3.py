def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"found {target} in {iterations} iterations")
            return
        elif arr[mid] < target: # Move the left pointer to the right
            left = mid + 1

        else: 
            right = mid - 1 # Move the right pointer to the left
    print(f"{target} not found after {iterations} iterations")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(numbers, 7)

def counter(n):
    if n == 0:
       print("stop")
       return
    print(n)
    counter(n - 1)



counter(5) 
            
            