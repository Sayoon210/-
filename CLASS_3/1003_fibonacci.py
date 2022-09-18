def fibonacci(N, resList:list, n):
  f1 = 0
  f2 = 1
  f = 1
  for x in range(n,N+1):
    f = f1+f2
    f1 = f2
    f2 = f
  resList[0] = f1
  resList[1] = f

T = int(input())

for t in range(T):
  resList = [0,0]
  N = int(input())
  if N == 0:
    resList[0] += 1
  elif N == 1:
    resList[1] += 1
  elif N == 2:
    resList[0] += 1
    resList[1] += 1
  else:
    fibonacci(N, resList, 2)
  print(f"{resList[0]} {resList[1]}")  