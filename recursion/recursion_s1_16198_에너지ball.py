import copy

def energy(_ball):

  if len(_ball) == 3:
    res = _ball[0] * _ball[2]
    return res
  else:
    a = list()
    i = 1
    while i < len(_ball)-1:
      res = _ball[i-1] * _ball[i+1]
      _ball2 = copy.deepcopy(_ball)
      del _ball2[i]
      res += energy(_ball2)
      a.append(res)
      i+=1
    return max(a)


num = int(input())
ball = list(map(int, input().split()))
result_m = list()
print(energy(ball))
