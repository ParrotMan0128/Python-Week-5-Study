import random as r;

initialMoney = 50;
goalMoney = 250;

win = 0;

cash = initialMoney;

for i in range(0, 100):

    random = r.randint(1, 2);

    if (random == 1):

        cash = cash + 1;

    elif (random == 2):

        cash = cash - 1;

    if (cash == goalMoney):

        win = win + 1;

print("초기 금액 : $" + str(initialMoney));
print("목표 금액 : $" + str(goalMoney));
print("100번 중에서 " + str(win) + "번 성공");
