import turtle
t = turtle.Turtle()
s = turtle.Screen()
colorsbg = ['#29C7BD', '#1487B0', '#14B06C', '#10BA2D', '#45DB21', '#FFFFFF']
colorsrb = ['#FE0002', '#D80027', '#A1015D', '#63009E', '#2A00d5', '#0302FC']
colorsrg = ['#00FF00', '#95FF66', '#C8FFb3', '#FFC2AC', '#FF6B5E', '#FF0000']
colorsjg = ['#88CBB9', '#76B4AD', '#649C9D', '#537E86', '#43616F', '#334358']
colors_dict = {"bg":colorsbg, "rb":colorsrb, "rg":colorsrg, "jg":colorsjg}
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

# creates a certain amount of semi erased spirals that looks pretty cool, amt of times is based on user input
count = int(input("How many times do you want to repeat the spiral? "))
print("Function has been repeated " + str(count) + " times.")
c = input("What color do you want it to be? bg(blue-green), rg(red-green), rb(red-blue), jg(jade-green). Say exactly like that: ")
def draw_spiral(count):
  if count == 0:
    return
  
  #makes spiral and changes color based on user input
  colors = colors_dict[c]
  for x in range(200):
      t.pencolor(colors[x % len(colors)])
      t.width(x / 300 + 3)
      t.forward(x)
      t.left(59)
  t.right(239)
  #deletes spiral somewhat which gives it cool remenants
  for x in range(200, 0, -3):
    t.pencolor('black')
    t.width(x / 100 + 10)
    t.forward(x)
    t.right(59)
    
  draw_spiral(count - 1)
  
draw_spiral(count)
turtle.done()
