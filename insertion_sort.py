import printStep


def insertion_sort(A) :
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
         #정렬된 부분의 맨 뒤에서 앞으로 가면서 key보다 큰 요소는 모두 한 칸씩 뒤로 이동,#이동이 멈춘 위치에 원래의A[i]를 저장(끼워 넣기)
        while j>=0 and A[j] > key:
            A[j + 1] = A[j] 
            j -= 1
        A[j + 1] = key 
        printStep(A,i)
