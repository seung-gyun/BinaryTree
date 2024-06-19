#Binary Tree

N = int(input()) # 입력 데이터 개수
A = list(map(int, input().split())) # 개수
A.sort()

M = int(input()) # 찾아야할 개수
target_list = list(map(int, input().split())) # 찾아야할 값



for i in range(M): # 찾아야 하므로 M을 기준으로 하기
    find = False
    target = target_list[i]
    
    start = 0
    end = len(A)-1

    while start<=end:
        midi = (start+end)//2
        midv = A[midi]
        
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else :
            find = True
            break
    if find:
        print(1)
    else:
        print(0)





