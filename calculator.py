number1 = input('Enter the number : ')
num1 = int(number1)
sign = input('Enter the sign ')
number2 = input('enter the number ')
num2 = int(number2)
if sign == '+':
    print('Your result is ' + str(num1 + num2))
elif sign == '-':
   print('Your result is ' + str(num1 - num2))
elif sign == '*':
   print('Your result is ' + str(num1 * num2))
elif sign == '/':
   print('Your result is :' + str(num1 / num2))
else:
   print('Plese enter + , -, *, or /')