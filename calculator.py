name = input("What is your name?:")
number1 = float(input ("Enter First Number: "))
number2 = float(input("Enter Second Number:"))

add = number1 + number2
sub = number1 - number2
multi = number1 * number2
div = number1 / number2
floor = number1 // number2

print(f"---Hi, {name}. Here are your results---")
print(f"{number1} + {number2} = {add}")
print(f"{number1} - {number2} = {sub}")
print(f"{number1} * {number2} = {multi}")
print(f"{number1} / {number2} = {div}")
print(f"{number1} // {number2} = {floor}")