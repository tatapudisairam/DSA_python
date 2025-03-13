print("\n.........................Merge Sorting.........................\n")

def merge_sort(A, left, right):
    if left<right:
        mid = (left + right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right+1)
    while i<=mid and j<=right:
        if A[i] <= A[j]:
            B[k] = A[i]
            i = i+1
        elif A[i] > A[j]:
            B[k] = A[j]
            j = j+1
        k = k+1
    while i<=mid:
        B[k] = A[i]
        i = i+1
        k = k+1
    while j<=right:
        B[k] = A[j]
        j = j+1
        k = k+1
    for m in range(left, right+1):
        A[m] = B[m]

def merge_2(A, left, mid, right):
    i = left
    j = mid+1
    k = 0
    B = [0] * (right-left+1)
    while i<=mid and j<=right:
        if A[i] <= A[j]:
            B[k] = A[i]
            k = k+1
            i = i+1
        elif A[i] > A[j]:
            B[k] = A[j]
            k = k+1
            j = j+1
    while i<=mid:
        B[k] = A[i]
        i = i+1
        k = k+1
    while j<=right:
        B[k] = A[j]
        j = j+1
        k = k+1
    k = 0
    while left<=right:
        A[left] = B[k]
        left = left+1
        k = k+1

n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
merge_sort(l1, 0, len(l1)-1)
print("Sorted list: ", l1)