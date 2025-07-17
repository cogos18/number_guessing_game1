# __main__.py | cogos18
# 17/07/2025  | 2:11 PM

"""
Description:
A simple number guessing game written in Python.

Created as a practice project.
"""
# Modules
from random import randint # For creating randomly generated numbers


# The number of attempts made by the player
attempts: int = 0
# Make the player try and guess the number in 15 attempts
max_attempts: int = 15

# The range that the number will be created within, which should be between 1 and 100
number_range: dict[str, int] = {
    "min": 1,
    "max": 100
}

# Create a randomly-generated number for the player to guess
number_to_guess: int = randint(number_range["min"], number_range["max"])


# Instruct the user to guess a number between 1 and 100
def get_answer(_prompt: str = f"Enter a number between {number_range['min']} and {number_range['max']}") -> str:
    return input(f"{_prompt}: ")


# Check if the answer is valid and/or correct
def _check_answer(answer: str, guess: int, number_range: dict[str, int]) -> dict:
    # The results
    _result: dict = {
        "status": 0, # 0 = incorrect, 1 = correct and -1 = something went wrong
        "msg": "" # The message that is displayed after each attempt.
    }

    try:
        # Convert the answer to a number
        _answer: int = int(answer)

        # Check if the answer is within range
        if not (_answer > number_range['min'] and _answer < number_range['max']):
            _result.update({"msg": "Please choose a number with the range"})
            pass

        # Check if the answer is correct
        if _answer < guess:
            _result.update({"msg": "Too low!"})
        elif _answer > guess:
            _result.update({"msg": "Too high!"})
        else:
            _result.update({"status": 1, "msg": "Correct!"})
    except ValueError:
        _result.update({"msg": "Please choose a valid number"})
    except Exception as err:
        _result.update({"status": -1, "msg": str(err)})

    return _result

def main() -> None:
    global number_to_guess, number_range, attempts, max_attempts
    while True:
        # Stop if there are 15 failed attempts
        if attempts >= max_attempts:
            break

        # Prompt the user to enter a number between 1 and 100
        guess: str = get_answer()

        # Check if the answer is correct
        _result: dict = _check_answer(guess, number_to_guess, number_range)

        if _result["status"] <= -1:
            print("Something went wrong: " + _result["msg"])
        elif _result["status"] == 0:
            print(_result["msg"])
            attempts += 1
        elif _result["status"] >= 1:
            print(_result["msg"])
            break

    print(f"""Game over!

# RESULTS ################
Attempts: {attempts}/{max_attempts}
Correct answer: {number_to_guess}
##########################
""")

if __name__ == "__main__":
    main()
    input("Press enter to exit.")