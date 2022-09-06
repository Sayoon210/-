# input 받기
number = list(map(int, input().split()))
noHearList = list()
noSeeList = list()

# 목록과 문제 받기
for n in range(number[0]):
  noHearList.append(input())
for m in range(number[1]):
  noSeeList.append(input())

interSet = set(noHearList) & set(noSeeList)
nameList = list(interSet)
nameList.sort()
print(len(nameList))
for name in nameList:
  print(name)


