test_c = int(input())

while test_c > 0:
  r = input()
  remind = 0
  result = 0
  for i in r:
    if i == 'O':
      result += 1 + remind
      remind += 1
    else:
      remind = 0
  print(result)
  test_c -= 1