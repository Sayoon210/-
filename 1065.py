def check(n):
  a = int(n/100)
  b = int((n-a*100)/10)
  c = int((n-a*100-b*10))
  fst = a-b
  scn = b-c
  if fst == scn:
    return 1

  return 0

result = 0
num = int(input())
if num < 100 :
  result = num
else:
  result += 99

while num > 99:
  result += check(num)
  num -= 1

print(result)