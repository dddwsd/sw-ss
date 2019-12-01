'''
n개의 정수가 입력으로 주어진다

연속하여 몇개의 정수를 골라 합을 구할 수 있다
연속하는 정수를 골라 합을 구할 때, 그 합의 최대를 구함

지금까지의 총합 vs 현재 num
총합 > 현재 : 총합을 유지
총합 < 현재 : 현재부터 다시시작
'''

tc = int(input())
for index in range(1,tc+1):
    n = int(input())
    num = list(map(int,input().split()))
    dp,dp[0] = [0 for _ in range(n)],num[0]
    for i in range(1,n):
        dp[i] = max(num[i] + dp[i-1],num[i])
    print("#{} {}".format(index,max(dp)))
            
            