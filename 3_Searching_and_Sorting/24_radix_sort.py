print("\n.........................Radix Sorting.........................\n")

def radix_sort(A):
    n = len(A)
    maxsize = max(A)
    maxdigits = len(str(maxsize))
    l = []
    bins = [l] * 10
    for i in range(maxdigits):
        for j in range(n):
            digit = int((A[j]/pow(10, i)) % 10)
            if len(bins[digit])>0:
                bins[digit].append(A[j])
            else:
                bins[digit] = [A[j]]
        k = 0
        for j in range(10):
            if len(bins[j]) > 0:
                for y in range(len(bins[j])):
                    A[k] = bins[j].pop(0)
                    k = k+1

n = int(input("Enter how many integers you want to insert into the list: "))
inputt = input("Enter the elements separated by a space: ")
inputt.strip()
l1 = list(map(int, inputt.split(" ")))
print("Original list:", l1)
radix_sort(l1, 0, len(l1)-1)
print("Sorted list: ", l1)