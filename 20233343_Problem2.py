fruits = ["사과", "감귤"];

while (len(fruits) <5 ):

  fruit = input("어떤 과일을 저장할까요?>>> ");

  if (fruit in fruits):

    print("동일한 과일이 있습니다.");
    continue;

  fruits.append(fruit);
  print("입력이 " + str(5 - len(fruits)) + "번 남았습니다.");
  
print("5개과일은 " + str(fruits) + "입니다");
