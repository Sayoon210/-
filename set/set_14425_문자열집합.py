inputNumbers = list(map(int, input().split()))
set1 = set([])
stringList = list()
set2 = set([])

for m in range(inputNumbers[0]):
  set1.update([input()])

for n in range(inputNumbers[1]):
  ip = input()
  stringList.append(ip)
  set2.update([ip])

interSet = set1 & set2
result = 0

for x in stringList:
  if x in interSet:
    result += 1

print(result)


# S집합은 상관 없으나 M집합에서 겹치는 것들을 함부로 set으로 만들면 중복을 허용하지않아 값이 이상해짐.
# 따라서 M집합은 set을 만듦과 동시에 list도 만들어서 원 입력값들을 보존해야한다.