def notSelfNum(notSelfList:list):
  for i in range(1, 10000):
    num = str(i)
    res = i
    for x in num:
      res += int(x)
    if res > 10000:
      pass
    else:
      notSelfList.append(res)


notSelfList = []
notSelfNum(notSelfList)
for selfNum in range(1, 10000):
  if selfNum in notSelfList:
    notSelfList.remove(selfNum)
  else:
    print(selfNum)
