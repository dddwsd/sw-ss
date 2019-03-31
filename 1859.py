tc = int(input())
for i in range(0,tc):
    n = int(input())    
    sale = list(map(int,input().split()))
    result = 0
    index = n-1
    # 함수호출을 통해서 최대값을 찾지 않는 것이 포인트
    for j in range (n-2,-1,-1):
        if sale[j] < sale[index] :
            result += sale[index] - sale[j]
        else:
            index = j
    print("#"+str(i+1)+' '+str(result))
    