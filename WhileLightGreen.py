GreenLightWords = ["green", "Green", "G", "g"];

while True:

    light = input("[!] 신호등 색상을 입력하시오\n>> ");
    if light in GreenLightWords:
        break

print("[!] 전진!");