# input 받기
dummy = input()
set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))

print(len(set1 ^ set2))

