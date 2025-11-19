#Sum the Array
N = int(input("Enter size of array: "))
A = list(map(int, input("Enter array elements: ").split()))
total = 0
for num in A:
    total += num
print("Sum of array elements:", total)
