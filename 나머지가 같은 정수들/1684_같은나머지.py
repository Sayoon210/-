
import math
# 연속된 수들의 최대공약수 구하기
def GCD(a, b, cnt, nList:list):
  res = math.gcd(a,b)
  cnt += 1
  if cnt == len(nList):
    return res
  return GCD(res, nList[cnt], cnt, nList)
  
inputNum = int(input())
NList = []
resultList = []
NList = list(map(int, input().split()))
NList.sort()

nList = []

for n in range(0, len(NList)-1):
  nList.append(NList[n+1] - NList[n])
  
if len(nList) == 1:
  resultList.append(nList[0])
elif len(NList) == 1:
  resultList.append(NList[0])
else:
  gcd = GCD(nList[0], nList[1], 1, nList)


if len(NList) == 1:
  pass
elif len(nList) != 1 and gcd != 0:
  resultList.append(gcd)

resultList.sort()
for answer in resultList:
  print(answer, end=' ')

