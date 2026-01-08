import random
from helper import difficulty

def select_number(limit: int) -> int:
    return random.randint(1, limit)

def get_number_of_tries(difficulty_input: int) -> int:
    tries = difficulty.Difficulty.get_dificulty_from_value(difficulty_input)
    if tries is None or difficulty_input > 3:
        return 0
    return tries.value

def main():
    while True:
        number_to_guess = select_number(limit=100)
        print('Hello this is a guessing the number game \n the computer has chosen a number between 1 and 100')
        difficulty_input = input("Choose a difficulty level:\n easy (1) -> 10 tries\n medium(2) -> 5 tries\n hard(3) -> 3 tries: \n\n Enter anything else to exit\n Your difficulty : ")
        difficulty_value =  get_number_of_tries(int(difficulty_input))

        if difficulty_value == 0:
            print('You chose a false difficulty level')
            return 0

        tries = 0
        while tries < difficulty_value:
            value = int(input("Tell me your guess : \n\n"))
            if value == number_to_guess:
                print("Congratulations! You guessed the number!")
            tries += 1
            if value > number_to_guess:
                print('You guessed the number too high!')
            elif value < number_to_guess:
                print('You guessed the number too low!')

        print('You did not guess the number, therefore you lose')
        print('The number was ' + str(number_to_guess) + '\n\n')

if __name__ == '__main__':
    main()
