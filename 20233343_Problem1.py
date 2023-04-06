total = 0;
passCount = 1;

while(passCount <= 5):

    i = int(input(str(passCount) + "번째 양수를 입력하십시오.\n>> "));

    if (i > 0):

        passCount = passCount + 1;
        total = total + i;

    else:

        print("[!] 양수를 입력해주세요.");
        continue;

print("입력된 양수의 합은 " + str(total) + "입니다.");
    