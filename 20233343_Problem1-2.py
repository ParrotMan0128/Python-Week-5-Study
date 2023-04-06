total = 0;

for i in range(1, 6):

    n = int(input(f"{i}번째 정수를 입력하세요!!>>>"));

    if (n < 0):

        print("0이하의 정수는 처리할 수 없습니다.");
        continue;
    
    total = total + n;

print(f"입력된 5개 정수의 합은 {total}입니다.");
