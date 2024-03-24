"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.shape("turtle") # 거북이 모양 생성하고 추가
t.color('red') # 테두리 컬러
t.fillcolor("yellow") # 생성된 거북이 내부 컬러
t.pensize(5) # 그리는 펜사이즈
t.begin_fill()# 실행

for i in range (5):
  t.forward(50)
  t.left(72)
  t.forward(50)
  t.right(144)
t.end_fill()#종료
screen.mainloop()
