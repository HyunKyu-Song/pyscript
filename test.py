from datetime import datetime
import turtle

now = datetime.now()
print(now.strftime("%y-%m-%d"))

t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)