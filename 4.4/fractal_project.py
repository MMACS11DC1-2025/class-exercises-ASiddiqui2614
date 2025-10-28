import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['#29C7BD', '#1487B0', '#14B06C', '#10BA2D', '#45DB21', '#FFFFFF']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

# Infinite loop to continuously draw and erase spiral pattern

while True:
  for x in range(200):
    t.pencolor(colors[x % len(colors)])
    t.width(x / 300 + 3)
    t.forward(x)
    t.left(59)
  t.right(239)
  
  for x in range(200, 0, -3):
    t.pencolor('black')
    t.width(x / 100 + 10)
    t.forward(x)
    t.right(59)