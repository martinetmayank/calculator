from product import product

run = True
while run:
    print('What you want to do?\n' + '1. Add\n' + '2. Subtract\n' + '3. Product\n' + '4. Divide\n' + 'q. quit\n')
    option = input()
    if option == 'q':
        run = False

    value_x = int(input('Enter value: '))
    value_y = int(input('Enter value: '))

    if option == '1':
        pass

    elif option == '2':
        pass

    elif option == '3':
        product(value_x, value_y)

    elif option == '4':
        pass