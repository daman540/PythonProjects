# Created 12/28/21
# Note: No input checks are written
import random
options = ["1 to 10", "1 to 100", "1 to 1000", "Make up your own numbers"] # Make up numbers will always be at the end

# Gives the user options to choose from
def menu():
    x = 1
    for o in options:
        print(str(x) + ") Choose from " + o)
        x += 1
    # Number must be between range
    while True:
        response = int(input("Your choice: "))
        if (response >= 1 and response <= len(options)):
            break
        else:
            print("INVALID ENTRY, TRY AGAIN")
    if (response == len(options)):
        option_end()
        return
    elif(response == 1):
        starting_point = 1
        ending_point = 10
    elif(response == 2):
        starting_point = 1
        ending_point = 100
    elif(response == 3):
        starting_point = 1
        ending_point = 1000
    main(starting_point, ending_point)


# If user picks the option at the end - "Make up your own numbers"
def option_end():
    starting_point = int(input("Starting number: "))
    ending_point   = int(input("Ending number  : "))
    main(starting_point, ending_point)

# Runs the number guessing game
def main(start, end):
    number_to_guess = random.randint(start, end)
    guesses = 0
    while True:
        response = int(input("Your guess: "))
        guesses += 1
        if (response == number_to_guess):
            print("Good job! The number was " + str(number_to_guess))
            if (guesses == 1):
                print("It took 1 guess to get the correct number, nice!")
            else:
                print("It took " + str(guesses) + " guesses to get the correct number, nice!")
            break
        elif(response < number_to_guess):
            print("Higher")
        elif(response > number_to_guess):
            print("Lower")
    
menu()
# Finished 12/29/21