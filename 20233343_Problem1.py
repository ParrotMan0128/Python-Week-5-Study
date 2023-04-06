total = 0;
count = 1;

while(count <= 5):

    n = int(input(f"{count}번째 정수를 입력하세요!!>>>"));

    if (n < 0):

        print("0이하의 정수는 처리할 수 없습니다.");
        continue;

    count = count + 1;
    total = total + n;

print(f"입력된 5개 정수의 합은 {total}입니다.");
