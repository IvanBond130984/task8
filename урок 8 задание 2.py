print('Введите количество элементов списка: ')
n=int(input())
lsn=[]
new_lsn=[]
for i in range(n):
    temp=input('Введите число: ')
    temp=int(temp)
    lsn.append(temp)
if n%2==0:
    m=n//2
else:
    m=n//2+2
for j in range(1,m):
    if j==m-1:
        new_lsn.append(lsn[-j])
    else:
        new_lsn.append(lsn[-j])
        new_lsn.append(lsn[j-1])
print(*new_lsn)