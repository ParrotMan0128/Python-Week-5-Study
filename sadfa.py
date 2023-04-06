total = 0;
string = "";

for a in range (1, 11):

    if (a % 3 != 0):

        string = string + str(a) + " + ";
        total = total + a;

newString = string[0:len(string) - 3];

newString = newString + " = " + str(total);

print(newString);    