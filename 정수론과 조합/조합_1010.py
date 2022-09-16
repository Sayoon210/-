inputNum = int(input())

def factos(N):
  if N == 0:
    return 1
  res = 1
  for n in range(2,N+1):
    res *= n
  return res

for i in range(inputNum):
  inputSite = list(map(int, input().split()))
  print(int(factos(inputSite[1])/(factos(inputSite[0])*factos(inputSite[1]-inputSite[0]))))