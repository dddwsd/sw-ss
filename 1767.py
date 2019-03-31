import copy
from pprint import pprint

def check(fix_type,fix,start,end):
    # visited확인 선연결 불가능하면 False 가능하면 True
    if fix_type == 'x':
        for i in range(start,end):
            if maxinos[i][fix] == 1 or maxinos[i][fix] == 2:
                return False
        return True
    elif fix_type == 'y':
        for i in range(start,end):
            if maxinos[fix][i] == 1 or maxinos[fix][i] == 2:
                return False
        return True

def change(fix_type,fix,start,end,data):
    if fix_type == 'x':
        for i in range(start,end):
            maxinos[i][fix] = data
    elif fix_type == 'y':
        for i in range(start,end):
            maxinos[fix][i] = data
    

def DFS(index,length,core):
    global flag
    global result
    global r_core
    if index == len(cell):
        if flag == 0 :
            r_core = core
            result = length
            flag = 1
            return
        else:
            if core > r_core:
                r_core = core
                result = length
            elif core == r_core and length < result:
                result = length
            return

    x = cell[index][0]
    y = cell[index][1]
    if x == 0 or y == 0 or x == n-1 or y == n-1: 
        DFS(index+1,length,core+1)
    else:
        # 위
        if check('x',x,0,y) == True:
            change('x',x,0,y,2)
            length += y
            DFS(index+1,length,core+1)
            length -= y
            change('x',x,0,y,0)
        # 왼
        if check('y',y,0,x) == True:
            change('y',y,0,x,2)
            length += x
            DFS(index+1,length,core+1)
            length -= x
            change('y',y,0,x,0)
        # 오른
        if check('y',y,x+1,n) == True:
            change('y',y,x+1,n,2)
            length += n-x-1
            DFS(index+1,length,core+1)
            length -= n-x-1
            change('y',y,x+1,n,0)
        # 아래
        if check('x',x,y+1,n) == True:
            change('x',x,y+1,n,2)
            length += n-y-1
            DFS(index+1,length,core+1)
            length -= n-y-1
            change('x',x,y+1,n,0)
        #아무곳도 못갈경우
        else:
            DFS(index+1,length,core)

tc = int(input())
for i in range (0,tc):
    n = int(input())
    maxinos = [0 for j in range(n)]
    cell = []
    for j in range(0,n):
        list1 = list(map(int,input().split()))
        maxinos[j] = copy.deepcopy(list1)
        # maxinos[y][x]
        while True:
            if 1 in list1:
                cell.append((list1.index(1),j))
                # (x,y) 형식으로 cell에 삽입
                list1[list1.index(1)] = 0
            else:
                break          
    flag = 0
    result = 0
    r_core =0    

    DFS(0,0,0)
    print('#'+str(i+1)+' '+str(result))