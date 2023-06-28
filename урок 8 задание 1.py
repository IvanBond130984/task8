print('Введите количество элементов списка: ')
n=int(input())
lsi=[]
for i in range(n):
    temp=input('Введите число: ')
    lsi.append(int(temp))
r=lsi[len(lsi)-1::-1]
print(*r)