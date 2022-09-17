# 이항계수 = nCr

def factos(N):
  if N == 0:
    return 1
  res = 1
  for n in range(2,N+1):
    res *= n
  return res

inputSite = list(map(int, input().split()))
ihang = int(factos(inputSite[0])/(factos(inputSite[1])*factos(inputSite[0]-inputSite[1])))
print(ihang)