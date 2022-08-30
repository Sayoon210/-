# 이 문제의 핵심은 6661 6662와 같은 형태를 어떻게 정리할까? 인 듯 하다.
# 그냥 666부터 하나씩 세서 해당번째 루프의 숫자가 인풋이랑 같은 경우를 비교하면 그만이다.

# 666 들어가는 숫자 찾기 함수
def find(num):
  _num = str(num)
  i = 1
  while True:
    if _num[i] == '6':
      if _num[i-1] == '6' and _num[i+1] == '6':
        return True
    if _num[i+1] == '6':
      i += 1
    else:
      i += 3
    if i >= len(_num)-1:
      return False
    

    

number = int(input())
start = 666
count = 1
while True:
  #print(start)
  if number == 1:
    print("666")
    break
  start += 1
  if find(start):  
    count += 1
    if count == number:
      print(start)
      break

