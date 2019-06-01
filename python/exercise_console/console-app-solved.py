def main_menu():
    print()
    print('1. Perform routine A')
    print('2. Perform routine B')
    print('3. Quit')
    try:
        selection = int(input('Enter choice: '))
        if selection == 1:
            routine_a()
        elif selection == 2:
            routine_b()
        elif selection == 3:
            exit()
        else:
            print('Invalid Choice. Only numbers between 1 and 3 are allowed.')
            main_menu()
    except ValueError:
        print('The program is expecting a number between 1 and 3. Please try again.')
        main_menu()

def routine_a():
    print('Starting routine A...')
    print('.........')
    print('Finished!')
    main_menu()

def routine_b():
    print('Starting routine B...')
    print('.........')
    print('Finished!')
    main_menu()

main_menu()