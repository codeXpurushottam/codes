import turtle

t = turtle.Pen()
turtle.speed(100000000000)
turtle.bgcolor("black")
colors = ["red", "purple", "blue", "green", "orange", "white"]
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100+1)
    t.forward(x)
    t.left(59)