import random
computer_number = random.randint(1,100)
difficulty_level = int(input('Level of difficulty. 1 for 10 attempts, 2 for 5 attempts, 3 for 3 attempts.'))
attempts = {
    1: 10,
    2: 5,
    3: 3
}
print(attempts[difficulty_level])
print(computer_number)
for i in range (1, attempts[difficulty_level]):
    user_number = int(input("Your guess"))
    if 15 >= (user_number - computer_number) > 10:
        print('Go lower for less than 15 or equal 15')
    elif (user_number - computer_number) > 15:
        print('Go lower for more than 15')
    elif 10 >= (user_number - computer_number) > 5:
        print('Go lower for less than 10 or equal 10')
    elif (user_number - computer_number) > 10:
        print('Go lower for more than 10')
    elif 5 >= (user_number - computer_number) > 0:
        print('Go lower for less than 5 or equal 5')
    elif (user_number - computer_number) > 5:
        print('Go lower for more than 5')

    elif 0 < (computer_number - user_number) <= 15 :
        print('Go higher for less than 15 or equal 15')
    elif (computer_number - user_number) > 15:
        print('Go higher for more than 15')
    elif (computer_number - user_number) <= 10:
        print('Go higher for less than 10 or equal 10')
    elif (computer_number - user_number) > 10:
        print('Go higher for more than 10')
    elif (computer_number - user_number) <= 5:
        print('Go higher for less than 5 or equal 5')
    elif (computer_number - user_number) > 5:
        print('Go higher for more than 5')
    else:
        print('Right! This is the number!')
