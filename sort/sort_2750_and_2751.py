a = int(input())
n = list()
while a > 0:
    n.append(int(input()))
    a -= 1
n.sort()
for i in n:
    print(i)