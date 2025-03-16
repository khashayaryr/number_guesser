import random

def input_validator(input):
    if not input.isdigit():
        print("Please enter a valid number between 1 and 100")
        return False
    if int(input) < 1 or int(input) > 100:
        print("Please enter a valid number between 1 and 100")
        return False
    return True


def main():
    selected_number = random.randint(1, 100)
    score = 100
    while True:
        user_input = input("Enter a number between 1 and 100 (or 'q' for exiting): ")
        if user_input.lower() == "q":
            break
        validity = input_validator(user_input)
        if not validity:
            continue
        user_input = int(user_input)
        if user_input == selected_number:
            print(f"Congratulations! You win. Your score is {score}.")
            break
        elif user_input < selected_number:
            print("Guess a higher number.")
            score -= 10
        else:
            print("Guess a lower number.")
            score -= 10
        score = max(score, 0)


if __name__ == '__main__':
    main()
