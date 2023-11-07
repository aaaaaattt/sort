def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :  # 0,1,2,3 ... , n-2
        least = i
        for j in range(i+1, n) :#i+1,i+2,i+3, ... , n-1
            if(A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A,i+1)

def printStep(arr,val) :
    print(" Step %2d = " %val, end='')
    print(arr)


selection_sort([4,3,2,1])