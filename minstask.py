class minStack(object):
  def __init__(self):
    self.stk = []
  
  def push(self, x):
    self.stk.append((x, min(x, self.getMin()) if len(self.stk) else x))

  def pop(self):
    return self.stk.pop()[0]

  def top(self):
    return self.stk[-1][0]

  def getMin(self):
    return self.stk[-1][1]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
