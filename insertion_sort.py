def insertion_sort(A):

    for i in range(1,len(A)):
        current = A[i]

        for j in range(i,-1,-1):
            
            if current < A[j]:
                A[j+1] = A[j]
                A[j] = current
                current = A[j]


arr = ['B','C','D','A','E','H','G','F']
print('Before sorting :',arr)
insertion_sort(arr)
print('After sorting :',arr)

