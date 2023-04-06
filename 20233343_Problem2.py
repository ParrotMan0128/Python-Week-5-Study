fruits = ["사과", "감귤"];
passCount = 0;

while (len(fruits) < 5):

    s = input("저장할 과일을 입력하시오.\n>> ");

    if (s in fruits):

        print("이미 동일한 과일이 저장되어있습니다.");

    else:

        fruits.append(s);
        print("입력이 " + str(5 - len(fruits)) + "번 남았습니다.");

print("5개 과일은 " + str(fruits) + " 입니다.");

