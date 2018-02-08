def game():
    input1 = int(input('Enter a number: '))
    input2 = int(input('Enter one more number: '))

    if input1 % 4 == 0:
        print('Your first number is even and can be divided by 4')
    elif input1 % 2 == 0:
        print('Your first number is even')
    elif input1 % 2 != 0:
        print('Your first number is odd')

    remainder = input1 % input2

    if remainder == 0:
        print('First number divides by the second number without remainder')
    elif remainder != 0:
        print('First number divided by the second one returns a remainder of {}'.format(remainder))


question = 'Yes'
while (question == 'Yes'):
    game()
    question = input('Do you want to play one more time? Yes/No \n')
else:
    print('Good Bye')

