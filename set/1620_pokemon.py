# input 받기
number = list(map(int, input().split()))
nameList = list()
problemList = list()

# 목록과 문제 받기
for n in range(number[0]):
  nameList.append(input())


for m in range(number[1]):
  inp = input()
  try:
    intp = int(inp)
    problemList.append(intp)
  except:
    problemList.append(inp)


for problem in problemList:
  if type(problem) == int:
    pokemonName = nameList[problem-1]
    print(pokemonName)
  else:
    pokemonNum = nameList.index(problem)+1
    print(pokemonNum)
