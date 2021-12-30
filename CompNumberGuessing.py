from random import randint
import time
mid_point = 0

# Asks user for range of guess, lowest to biggest.
# The numbers must not be negative.
def menu():
    print("The computer will guess a number from your range.")
    while True:
        starting_point = int(input("Give me a starting point: "))
        if(starting_point < 0):
            print("Invalid entry, must be a positive number.")
        else:
            break
    while True:
        ending_point = int(input("Give me an ending point : "))
        if(ending_point < 0):
            print("Invalid entry, must be a positive number.")
        else:
            break
    main(starting_point, ending_point)


def main(start, end):
    mid_point = int((start + end) // 2)
    while True:
        num_to_guess = int(input("Number to guesss: "))
        if(num_to_guess > start and num_to_guess < end):
            break
        else:
            print("Invalid entry, must be between given range. " + start + " to " + end)
    comp_start = start
    comp_end = end
    guesses = 0
    while mid_point != num_to_guess:
        guesses += 1
        if mid_point < num_to_guess:
            print("I guessed... " + str(mid_point))
            comp_start = mid_point
        elif mid_point > num_to_guess:
            print("I guessed... " + str(mid_point))
            comp_end = mid_point
        #see_values(start, end, mid_point) # Uncomment for testing
        mid_point = (comp_start + comp_end) // 2
        time.sleep(1)
    # Out of while loop
    guesses += 1
    print("I guessed... " + str(mid_point))
    print("I got it! Took me " + str(guesses) + " guesses")


# Used for testing, seeing values
def see_values(a, b, c):
    print("Front: " + str(a) + '\n' + "End: " +  str(b) + '\n' + "Mid Point: " + str(c))

menu()
