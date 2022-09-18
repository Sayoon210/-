class SetFunc:
  def __init__(self):
    self.setM = set()
  def add(self, n):
    self.setM |= {n}
  def remove(self, n):
    self.setM -= {n}    
  def check(self, n):
    interSet = self.setM & set([n])
    if len(interSet):
      print(1)
    else:
      print(0)
  def toggle(self, n):
    interSet = self.setM & set([n])
    if len(interSet):
      self.remove(n)
    else:
      self.add(n)
  def all(self):
    self.setM = set([str(i) for i in range(1, 21)])
  def empty(self):
    self.setM -= self.setM


N = int(input())
SET = SetFunc()
for a in range(N):
  order = list(input().split())
  if order[0] == "add":
    SET.add(order[1])
  elif order[0] == "remove":
    SET.remove(order[1])
  elif order[0] == "check":
    SET.check(order[1])
  elif order[0] == "toggle":
    SET.toggle(order[1])
  elif order[0] == "all":
    SET.all()
  elif order[0] == "empty":
    SET.empty()