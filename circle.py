import turtle;
import random as r;

t = turtle.Turtle();
t.shape("turtle");
t.speed(300);

tryCount = int(turtle.textinput("", "숫자를 입력하시오"));

for i in range (tryCount):

    t.forward(1 + i /4);
    t.left(30 - i / 12);

turtle.mainloop();
turtle.bye();
