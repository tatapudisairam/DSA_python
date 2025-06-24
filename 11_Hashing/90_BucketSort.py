print("\n.........................Bucket Sorting.........................\n")


def insertion_sort(L):
    n = len(L)
    for i in range(n):
        cvalue = L[i]
        position = i
        while position>0 and cvalue<L[position-1]:
            L[position] = L[position-1]
            position = position-1
        L[position] = cvalue

def bucket_sort(A):
    n = len(A)
    if n<=1:
        return
    maxElement = max(A)
    buckets = [[] for _ in range(10)]
    for i in range(n):
        index = (n*A[i])//(maxElement+1)
        if len(buckets[index]) == 0:     #or we can directly use buckets[index].append(A[i])
            buckets[index] = [A[i]]
        else:
            buckets[index].append(A[i])
    
    for i in range(10):
        insertion_sort(buckets[i])
    
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k = k+1

A = [62, 250, 835, 947, 652, 29]
print("Before sorting:", A)
bucket_sort(A)
print("After sorting:", A)
