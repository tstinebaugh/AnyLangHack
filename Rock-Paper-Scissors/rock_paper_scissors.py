import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    beats = {
        Action.Rock: Action.Scissors,
        Action.Paper: Action.Rock,
        Action.Scissors: Action.Paper
    }
    
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif beats[user_action] == computer_action:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")
        
if __name__ == '__main__':
    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

