def calculate():
    operation = input('''
Please Type the math operation you would like to complete:
+ for addition
- for Subtraction
* for Multiplication
/ for division
''')

    n1 = float(input('enter the First number: '))
    n2 = float(input('enter the Second number: '))

    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('You have entered a wrong math operator!')
    again()

def again():
    calculation_again = input('''
Do you want to Calculate again?
Please type Y for Yes or N for No
''')

    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('ok.')
    else:
        again()

calculate()