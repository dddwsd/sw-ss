'''
n,r
n com r의 값을 123456791로 나눈 나머지를 출력하라

https://wondangcom.com/714 참고

페르마의 정리
a가 정수 p가 소수일떄 a와 p가 서로소이면
a^p-1 = 1 (mod p)

(n! x (k!(n-k)!)-1) % p -> 우리가 구하는 식
a = n!
b = (k!(n-k)!)^-1
약분하면
a = n ~ n-k+1
b = k!

이떄 b는 분수이므로 %p가 분배법칙을 성립하지 않는다.
페르마의 정리를 변형하면
a*a^p-2 = 1 (mod p) 이고 따라서
a^p-2 = a^-1이다.
따라서 b^-1 = b^p-2를 만족하고
b^p-2는 분수가 아니기 때문에 분배법칙이 만족한다.
즉 ((a%p) * (b^p-2%p)) %p

cnt = 1  2  2
b =  1  2  
'''

t = int(input())
for tc in range(1,t+1):
    n,r = map(int,input().split())
    p,up,do = 1234567891,n,1
    for i in range(2,r+1):
        up = (up*(n-i+1))%p
        do = (do*i)%p
    if r == 0 or r == n : down = 0
    ind = p-2
    d = 1
    # 거듭 제곱 구하는 방법
    # 짝수일때는 계속 크기를 늘려나가다가
    # 홀수일때 결과값에 곱해줌
    # https://onsil-thegreenhouse.github.io/programming/problem/2018/03/29/problem_math_power/ 참조
    while ind>0:
        if ind%2 == 1:
            d *= do
            d %= p
            ind -= 1
        do = (do*do)%p
        ind /= 2
    print("#{} {}".format(tc,((up%p)*(d%p))%p))
        




        
        



