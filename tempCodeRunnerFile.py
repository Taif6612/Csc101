Example 2:
choice = input('''Please select the type of operation you want to perform: 
+ for addition 
- for subtraction 
* for multiplication 
/ for division''')
 
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
 
if choice == '+':
    print(number_1 + number_2)
 
elif choice == '-':
    print(number_1 - number_2)
 
elif choice == '*':
    print(number_1 * number_2)
 
elif choice == '/':
    print(number_1 / number_2)
 
else:
    print('You have not typed a valid operator, please run the program again.')