# 1차시도 : 브루트포스 => 실패!
# 2차시도 : 음수 양수 나눠서 비교 => 실패!
# 3차시도 : 비교가 끝난 것은 지운다 => 실패!
# 성공시도 : 으아닛 교집합을 구해주는 내장함수가 있을줄이야ㅋㅋㅋㅋ 뷰우웅신ㅋㅋㅋㅋ

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이렇게나 편한 집합계산을 이제야...
set1 = set(A)
set2 = set(B)
interSet = set1 & set2

for b in B:
  if b != B[0]: 
    print(' ', end='')
  if b in interSet:
    print('1', end='')
  else:
    print('0', end='')
  