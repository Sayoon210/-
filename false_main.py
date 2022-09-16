# 하씨 거의 다 푼거 같은데 이게 안풀리네 좆같은거...

# input 받기
allEven = True
allOdd = True
inputNum = int(input())
NList = []
resultList = []

for n in range(inputNum):
  ipNum = int(input())
  if ipNum % 2 != 0:
    allEven = False
  elif ipNum % 2 == 0:
    allOdd = False
  NList.append(ipNum)
NList.sort()

def checkR(nlist:list, M, R):
  #print(M)
  for n in nlist:
    #print(f"[{n}]", end=' ')
    #print(n%M, end='..')
    if n%M != R:
      #print("end")
      return False
  #print("end")
  return True
  
k = -1
start = NList[1]//2

# if not allEven and not allOdd:
#   k = -2
#   if start % 2 == 0:
#     start += 1
# elif allOdd or allEven:
#   resultList.append(2)

if allOdd or allEven:
  resultList.append(2)
  
# 두 수의 차로 두 수를 나누면 무조건 ㅆㄱㄴ
fstCheck = NList[1] - NList[0]
if checkR(NList, fstCheck, NList[0]%fstCheck):
  # if fstCheck**(1/2) == int:
  #   resultList.append(fstCheck**(1/2))
  for i in range(3, int(fstCheck**(1/2)) + 1):
    if (fstCheck % i == 0):
      resultList.append(i) 
      if ( (i**2) != fstCheck) : 
        resultList.append(fstCheck // i)
  resultList.append(fstCheck)


for M in range(NList[1]//2, 1, k):
  if not allEven and not allOdd:
    if k % 2 == 0:
      continue
  # print(M)
  if M in resultList:
    continue
  R = NList[0] % M
  if checkR(NList, M, R):
    for i in range(3, int(M**(1/2)) + 1):
      if (M % i == 0) and not i in resultList:
        resultList.append(i) 
        if ( (i**2) != n) and not M//i in resultList: 
          resultList.append(M // i)
    resultList.append(M)

resultList.sort()
for answer in resultList:
  print(answer, end=' ')