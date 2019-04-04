n = int(input())
list1 = []
for i in range(1,n+1):
    count = 0
    if '3' in str(i):
        count += str(i).count('3')
    if '6' in str(i):
        count += str(i).count('6')
    if '9' in str(i):
        count += str(i).count('9')
    if count == 0:
        list1.append(str(i))
    else:
        list1.append('-'*count)

print(' '.join(list1))