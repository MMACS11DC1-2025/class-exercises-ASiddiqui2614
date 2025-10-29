import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['#29C7BD', '#1487B0', '#14B06C', '#10BA2D', '#45DB21', '#FFFFFF']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

# creates a certain amount of semi erased spirals that looks pretty cool, amt of times is based on user input
count = int(input("How many times do you want to repeat the spiral? "))
def draw_spiral(count):
  if count == 0:
    return
    
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
    
  draw_spiral(count - 1)
  
draw_spiral(count)
turtle.done()
    