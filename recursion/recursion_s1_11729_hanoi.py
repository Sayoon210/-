def hanoi(size, s, m, e):
  if size == 1:
    print(f"{s} {e}")
  else:
    hanoi(size-1, s, e, m)
    print(f"{s} {e}")
    hanoi(size-1, m, s, e)

input_n = int(input())

print(2**input_n-1)
hanoi(input_n, 1, 2, 3)