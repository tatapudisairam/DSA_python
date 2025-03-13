print("\n.........................Bubble Sorting.........................\n")

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

def bubbble_sort_2(A):
    n = len(A)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                
n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
bubble_sort(l1)
print("Sorted list: ", l1)