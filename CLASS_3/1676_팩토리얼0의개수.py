N = int(input())

if N < 5:
  print('0')
elif N < 10:
  print('1')
else:
  i = 36288
  k = 11
  res = 2
  while k <= N:
    i *= k
    k += 1
    _i = str(i)
    while _i[-1] == '0':
      res += 1
      i //= 10
      _i = str(i)

  print(res)