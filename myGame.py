###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This mini project is based on
#               childhood counting game called Fizz Buzz
# Date:         14/05/2024
####################################

# Declare Constants and Initialize Variable
FIZZ = 'Fizz'
BUZZ = 'Buzz'
FIZZBUZZ = 'Fizz Buzz'
ONE = 1
ZERO = 0
FIVE = 5
THREE = 3
list_of_players = []
game_outcome = []
isValid = True
count = 0
player_index = 0

# To determine how many players are playing the game
players_number = int(input('Welcome to Fizz Buzz\nHow many players are playing?: '))

# To populate the list of players with each player
for players in range(players_number):
    list_of_players.append('player ' + str(players + ONE))

print(list_of_players)

# Start the game
while isValid:
    # Ask each player for the input
    player_entry = input('Please enter an input: ')
    # To ensure each player in the list are playing
    if player_index == len(list_of_players):
        player_index = ZERO
    player = list_of_players[player_index]
    # When the player is the first player
    if len(game_outcome) == ZERO:
        try:
            check_entry = int(player_entry)
            game_outcome.append((player, check_entry))
            count = check_entry
            count += ONE
            player_index += ONE
        except:
            print(f'{player_entry} is not valid number to begin the game, {player} try again')
    # When the player is not the first Player
    else:
        # Confirm if the player input is Fizz Buzz
        if player_entry == FIZZBUZZ:
            # Ensure if current number is divisible by 3 or 5
            if count % FIVE == ZERO and count % THREE == ZERO:
                # Add the player and the input as a tuple to the list of outcome
                game_outcome.append((player, player_entry))
                # End the game
                isValid = False
        # Confirm if player input is Fizz
        elif player_entry == FIZZ:
            # Ensure if current number is divisible by 3
            if count % THREE == ZERO:
                # Add the player and the input as a tuple to the list of outcome
                game_outcome.append((player, player_entry))
                # update the next number
                count += ONE
                # update the next player
                player_index += ONE
        # Confirm if player input is Buzz
        elif player_entry == BUZZ:
            # Ensure if current number is divisible by 5
            if count % FIVE == ZERO:
                # Add the player and the input as a tuple to the list of outcome
                game_outcome.append((player, player_entry))
                # update the next number
                count += ONE
                # update the next player
                player_index += ONE
        # If the user input is an integer
        else:
            try:
                # Validate it is an integer
                check_entry = int(player_entry)
                # check if the number entered is the next number in line
                if check_entry == count:
                    # Check if the user failed to recognize the number was divisible by 3 or 5
                    if check_entry % THREE == ZERO or check_entry % FIVE == ZERO:
                        # The player that got  it wrong lost
                        print(f'{player} is eliminated')
                        # End the game
                        isValid = False
                    else:
                        # Add the player and the input as a tuple to the list of outcome
                        game_outcome.append((player, check_entry))
                        # update the next number
                        count += ONE
                        # update the next player
                        player_index += ONE
                else:
                    # The number definitely is not next in line
                    print(f'{check_entry} is not the next number, '
                          f'{player} play again')
            except:
                # The input failed its validation and is not a number
                print(f'{player_entry} is not valid number')

# To get the required outcome from all players inputs
for outcome in game_outcome:
    print(outcome[1])