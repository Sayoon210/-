# x1 을 D로 나누면 나머지가 R1, 몫이 p1
# x2 을 D로 나누면 나머지가 R2, 몫이 p2

# 이때 R1 = R2 이므로
# x1 - D*p1 = x2 - D*p2
# 정리하면
# x1 - x2 = D(p1 - p2)

# 따라서!!!! 두수의 차는!!!! D의 배수가 된다!!!!
# 두수의 차가 D의 배수가 되지 못한다면! 실패한다!
# 따라서 두 수의 차의 최대공약수를 쫙 구한다!
# 1이면 바로 컷!

import math
# 연속된 수들의 최대공약수 구하기
def GCD(a, b, cnt, nList:list):
  res = math.gcd(a,b)
  if res == 1:
    return 0
  cnt += 1
  if cnt == len(nList):
    return res
  return GCD(res, nList[cnt], cnt, nList)
  
inputNum = int(input())
NList = []
resultList = []
for n in range(inputNum):
  ipNum = int(input())
  NList.append(ipNum)
NList.sort()

nList = []

for n in range(0, len(NList)-1):
  nList.append(NList[n+1] - NList[n])
  
if len(nList) == 1:
  resultList.append(nList[0])
else:
  gcd = GCD(nList[0], nList[1], 1, nList)
  
if len(nList) != 1 and gcd != 0:
  resultList.append(gcd)
  for i in range(2, int(gcd**(1/2)) + 1):
      if (gcd % i == 0):
        resultList.append(i) 
        if ( (i**2) != gcd): 
          resultList.append(gcd // i)
elif len(nList) == 1:
  for i in range(2, int(nList[0]**(1/2)) + 1):
      if (nList[0] % i == 0):
        resultList.append(i) 
        if ( (i**2) != nList[0]): 
          resultList.append(nList[0] // i)

resultList.sort()
for answer in resultList:
  print(answer, end=' ')

