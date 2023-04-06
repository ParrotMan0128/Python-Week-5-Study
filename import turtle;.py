import turtle;
import random as r;

t = turtle.Turtle();
t.shape("turtle");
t.width(5);

tryCount = int(turtle.textinput("", "숫자를 입력하시오"));

for i in range (tryCount):

    randomLength = r.randint(1,101);
    randomAngle = r.randint(-180, 181)

    t.forward(randomLength);
    t.right(randomAngle);

turtle.mainloop();
turtle.bye();
