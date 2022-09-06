# 개수까지 끄집어내야 한다...

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이렇게나 편한 집합계산을 이제야...
set1 = set(A)
set2 = set(B)
interSet = set1 & set2

# A의 카드 중 교집합에 포함되는 카드들의 개수
# 딕셔너리로 (카드숫자) : (개수) 형태
ADic = {}

for a in A:
  if a in interSet:
    if a in ADic.keys():
      ADic[a] += 1
    else:
      ADic[a] = 1
      
# 어차피 ADic의 keys는 교집합에 포함됨
# 따라서 바로 ADic의 키로 접근해 개수를 출력
for b in B:
  if b in interSet:
    print(ADic[b], end=' ')
  else:
    print('0', end=' ')



