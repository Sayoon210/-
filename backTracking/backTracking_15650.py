def backTrack(num, mSet:set, mList:list, M):
  mList[len(mList)-M] = num
  if M == 1:
    for _mList in mList:
      print(_mList, end=' ')
    print('')
  for x in mSet-set([l for l in range(1,num+1)]):
    if M == 1:
      return
    backTrack(x,mSet-set([num]), mList, M-1)



inputList = list(map(int, input().split()))
mSetList = [n for n in range(1, inputList[0]+1)]
M = inputList[1]
mSet = set(mSetList)
mList = [0 for k in range(1, inputList[1]+1)]
for num in mSet:
  backTrack(num, mSet, mList, M)