import turtle
t = turtle.Turtle()


def draw_smth(x, y):
    while True:
        t.penup()
        t.goto(-5 + x, -30 + y)
        t.pendown()
        t.circle(50)
        t.penup()

        t.goto(0 + x, -5 + y)
        t.stamp()
        
        t.goto(20 + x, 10 + y)
        t.stamp()
        
        t.goto(-20 + x, 10 + y)
        t.stamp()
        
        t.goto(15 + x, 5 + y)
        t.stamp()
        
        t.goto(-10 + x, 2 + y)
        t.stamp()
        
        t.goto(10 + x, 2 + y)
        t.stamp()
        
        t.goto(-15 + x, 5 + y)
        t.stamp()
        
        t.goto(20 + x, 40 + y)
        t.stamp()
        
        t.goto(-20 + x, 40 + y)
        t.stamp()
        
        break
draw_smth(0 ,0)