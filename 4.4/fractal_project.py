import turtle
t = turtle.Turtle()

def spiral(x, y):
  while x > 0:
    t.right(10 + x)
    t.forward(10 + y)
    
    x -= 1
spiral(30, 10)