# 이항계수 = nCr
# python의 연산범위는 15자리까지이다!

def factos(N, R):
  if N == 0:
    return 1
  res = 1
  for n in range(R+1,N+1):
    res *= n
  return res



inputSite = list(map(int, input().split()))
gaji = max(inputSite[1], inputSite[0]-inputSite[1])
ihang = int(factos(inputSite[0], gaji)/factos(inputSite[0]-inputSite[1],1))
while ihang >= 10007:
  ihang -= 10007

print(ihang)

