# input 받기
inputString = input()
limit = len(inputString)

comboList = []
i = 0
for k in range(1,limit):
  i = 0
  while True:
    comboStr = inputString[i:i+k]
    comboList.append(comboStr)
    if i+k == limit:
      break
    i += 1
comboList.append(inputString)
strSet = set(comboList)
print(len(strSet))
