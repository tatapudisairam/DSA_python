print("\n.........................Shell Sorting.........................\n")

def shell_sort(A):
    n = len(A)
    i = n//2 # here consider the i as gap
    while i>0:
        for j in range(i , n):
            cvalue = A[j]
            position = j
            while position>=i and A[position-i] > cvalue:
                A[position] = A[position-i]
                position = position-i
            A[position] = cvalue
        i = i//2

n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
shell_sort(l1)
print("Sorted list: ", l1)