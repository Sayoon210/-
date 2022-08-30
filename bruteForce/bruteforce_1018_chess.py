#홀짝 구분함수
def odd(num):
  if num/2 - int(num/2) != 0:
    return True
  else:
    return False

size = list(map(int,input().split()))
i = size[0]
board = list()

while i > 0:
  board.append(input())
  i -= 1

_h = 0
_l = 0


# 각 체스칸의 좌표는 (h,l)
# 왼쪽위는 (_h,_l)
# 0이 시작이면 7까지, 1이 시작이면 8까지인 방법
# 왼쪽위가 뭐인가에 따라서 하나만 하는게 아닌 둘다 해봐야한다는게 포인트

# 1. 8x8을 고른다
# 2. 왼쪽위가 흰색이냐 검은색이냐 두가지를 다 해서 갯수를 찾는다
# 3. 둘중에 작은 것만 남기고 다시 8x8을 돌린다
lst = list()
while _h <= size[0] - 8:
  _l = 0
  while _l <= size[1] - 8:
    # count를 2개로 잡은 이유는 왼쪽위를 W냐 B냐를 구분하기 위해
    # W,B순서는 좌표의 합이 짝수냐 홀수냐를 따져서 어떤 칸을 고쳐야하는지 구분가능하다.
    count = 0
    count_2 = 0
    start = board[_h][_l]
    h = _h
    while h <= _h+7:
      l = _l
      while l <= _l+7:
        if odd(h+l): # 좌표의 합의 홀짝 구분으로 WB를 나눈다.
          if board[h][l] == 'W':
            count += 1
          else:
            count_2 += 1
        else:
          if board[h][l] == 'B':
            count += 1
          else:
            count_2 += 1
        l += 1
      h += 1
    lst.append(count)
    lst.append(count_2)
    _l += 1
  _h += 1

print(min(lst))