test_c = int(input())

while test_c > 0:
  case = list(map(int,input().split(' ')))
  all = 0
  for i in case[1:]:
    all += i
  avg = all / case[0]
  succ = 0
  for j in case[1:]:
    if j > avg:
      succ += 1
  result = succ/case[0]*100
  print(f"{result:.3f}%")
  test_c -= 1