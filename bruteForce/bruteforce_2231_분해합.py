number = int(input())

i = 0

while i < number:
  i_s = str(i)
  res = i
  for s in i_s:
    res += int(s)

  if res == number:
    print(i)
    break
  i += 1

if i == number:
  print("0")