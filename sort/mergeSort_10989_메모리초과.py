def mergeSort(A, p:int, r:int):
  if p < r:
    q = (p+r) // 2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  i = p; j = q+1; t = 0
  tmp = [ 0 for i in range(len(A))]
  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp[t] = A[i]; t+=1; i+=1
    else:
      tmp[t] = A[j]; t+=1; j+=1
  while i <= q:
    tmp[t] = A[i]; t+=1; i+=1
  while j <= r:
    tmp[t] = A[j]; t+=1; j+=1
  i = p; t = 0
  while i <= r:
    A[i] = tmp[t]; t+=1; i+=1

N = int(input())
a = list()
for i in range(0,N):
  M = int(input())
  a.append(M)
mergeSort(a,0,N-1)
for x in a:
  print(x)