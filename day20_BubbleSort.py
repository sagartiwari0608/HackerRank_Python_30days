
n = int(input().strip())

a = list(map(int, input().rstrip().split()))

totalSwaps=0
# Write your code here
for i in range(n):
    numberOfSwaps=0
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numberOfSwaps+=1
    totalSwaps=totalSwaps+numberOfSwaps
    
    if numberOfSwaps==0:
        break

        
print("Array is sorted in "+str(totalSwaps)+" swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
