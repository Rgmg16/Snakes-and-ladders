import random

# Define the snakes and ladders as dictionaries
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 99}

# Define the dice roll function
def dice_roll():
    return random.randint(1, 6)

# Define the function to get the position of a player after applying snakes or ladders
def get_position(position):
    if position in snakes:
        new_position = snakes[position]
        print(f"Oh no! You landed on a snake. Move down to tile {new_position}.")
    elif position in ladders:
        new_position = ladders[position]
        print(f"Congratulations! You've landed on a ladder. Move up to tile {new_position}.")
    else:
        new_position = position
    return new_position

# Define the function to roll the dice and update the player's position
def update_position(player, position):
    dice_value = dice_roll()
    print(f"Player {player}: Current position: {position}, Dice roll: {dice_value}")
    position += dice_value
    position = get_position(position)
    return position

# Define the play function to simulate the game
def play():
    position_player1 = 0
    position_player2 = 0
    while position_player1 < 100 and position_player2 < 100:
        position_player1 = update_position(1, position_player1)
        if position_player1 >= 100:
            print("Player 1 wins!")
            break
        position_player2 = update_position(2, position_player2)
        if position_player2 >= 100:
            print("Player 2 wins!")
            break

# Start the game
play()
                 