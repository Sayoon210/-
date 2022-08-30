num = int(input())
index = num
a = list()
n = 1

while num > 0:
  a.append(list(map(int, input().split())) + [n])
  num -= 1
  n += 1
  
a.sort(reverse=True)

for i in a:
  if i == a[0]:
    i.append(1)
    continue
  count = 1
  for compare in a:
    if i[0] >= compare[0] :
      break
    elif i[1] < compare[1]:
      count += 1
  i.append(count)

a.sort(key = lambda a: a[2])

for p in a:
  if p == a[-1]:
    print(p[3])
  
  else:
    print(p[3], end=' ')
  

  
