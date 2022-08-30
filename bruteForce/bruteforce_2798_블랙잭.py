rule = list(map(int,input().split()))
card = list(map(int,input().split()))

card.sort()

for i in card:
  if i > rule[1]-3:
    del card[rule.index(i):]
    break

res = 0
a = list()
for i in card:
  res += i
  card.remove(i)
  for j in card:
    res += j
    for k in card[card.index(j)+1:]:
      res += k
      if res <= rule[1]:
        a.append(res)
      res -= k
    res -= j
  res = 0

print(max(a))