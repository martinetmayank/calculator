from product import product
from division import division
from ADD import Add
from subtract import subtract
from power import power

run = True
while run:
    print('What you want to do?\n' + '1. Add\n' + '2. Subtract\n' + '3. Product\n' + '4. Divide\n' + 'q. quit\n')
    option = input()


    if option == 'q':
        run = False

    if option != 'q':
        value_x = int(input('Enter value: '))
        value_y = int(input('Enter value: '))

        if option == '1':
            output = Add(value_x, value_y)

        elif option == '2':
            output = subtract(value_x, value_y)

        elif option == '3':
            output = product(value_x, value_y)

        elif option == '4':
            output = division(value_x, value_y)
        elif option == '5':
            output = power(value_x, value_y)
        print(str(output) + '\n')
