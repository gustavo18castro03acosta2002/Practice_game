# project 1 guess the number
import random as rand


def random_number():

    loop_swich = True

    while loop_swich:

        try:
            number_range_one = int(input(">Enter the number in which the range will start: "))
            number_range_two = int(input(">Enter the number in which the range will end: "))
            
            number = rand.randrange(number_range_one, number_range_two)
            loop_swich = False
        except ValueError as not_a_number:
            not_a_number = 'Those are not numbers dude!!!'; print(not_a_number)

        except UnboundLocalError as Fuck:
            Fuck = 'You didn\'t put those numbers Brah!!!'; print(Fuck)

    i = 0

    limit_lives = int(input(">How many live you want to have? "))

    while i != limit_lives:

        user_input = int(input(">Enter your guess: "))
        
        if user_input == number:

            print("Great you have won!")
            break

        elif user_input < number:

            print("That's too low, try again!")

        elif user_input > number:

            print("That's too high, try again!")

        else:
            try:
                pass
            except ValueError as not_a_number:
                not_a_number = 'A number is required, words are not allowed!!!'; print(not_a_number)

