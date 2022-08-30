# 10989 부터는 리스트의 정렬 알고리즘이 그리 잘 작동하지 않는 듯 하다...
# 날먹 개같이 실패!
# 퀵 정렬을 쓸까? https://mygumi.tistory.com/308
# 가운데 기준을 잡고
# 오른쪽과 왼쪽에서 부터 하나씩 요소를 잡는다
# 오른쪽은 기준보다 작은거, 왼쪽은 기준보다 큰거
# 오른쪽과 왼쪽을 서로 교차시킨다.
# 한쪽에서 어느 요소가 나오지 않는다면 다른 한쪽과 기준을 교차시킨다.
# 반복한다.

def quickSort(A, p:int, r:int):
  if p < r:
    q = partation(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)
    
def partation(A, p:int, r:int):
  x = A[r]
  i = p-1
  for j in range(p, r):
    if A[j] < x:
      i += 1
      A[i],A[j] = A[j],A[i]
  A[i+1],A[r] = A[r],A[i+1]
  return i+1

N = int(input())
a = list()
for i in range(0,N):
  a.append(int(input()))
quickSort(a,0,N-1)
for x in a:
  print(x)





# ㅄ이세요? 아니 재귀로 잘린 구간을 다시 퀵소트 해야지 참내ㅋㅋㅋ 그냥 자라ㅋㅋㅋ
