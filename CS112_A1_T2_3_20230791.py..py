# File: CS112_A1_T2_3_20230791.py.
# Purpose: Subtract a Square is a two-player game where players take turns removing coins.
#         players must remove a non-zero square number of coins, The player who removes the last coin wins
# Author: Olla Mohamed El-Fatih Hassan Nour
# ID: 20230791
# --------------------------------------------------------------------------------------------------------
# Display Welcome message and instructions
print("Welcome to Subtract a Square game")
print('This Game is a two-player Game Where Each Player Takes Turns on correctly subtracting '
      'a non-zero square number of coins From a Pile. '
      'To win, you must be the one who removes the last coin.')
total_c = 0  # assigning the total to an initial value
# Display query if Player wants specific number of coins or random number
player_Preference = input("would you like a random number of coins or a specific number of coins ?(ran/spe): ")
while player_Preference not in ["ran", "spe"]:  # To ensure that the player will choose either spe or ran
    print("please choose 'ran' or 'spe' only")
    player_Preference = input("would you like a random number of coins or a specific number of coins ?(ran/spe): ")
# Check if player_preference is equal to "ran" and assign value
if player_Preference == "ran":
    import random
    ran = random.randint(100, 800)
    total_c = ran
# Display Number of Coins for the user
    print("the random number of coins is : ", ran)
# Check if player_preference is equal to "spe" and assign value
elif player_Preference == "spe":
    while True:  # start a loop to make sure user enters a number from 100-800
        try:
            total_c = int(input("Please choose a number from 100 to 800: "))
            if 100 <= total_c <= 800:
                print("The chosen number is", total_c)  # Display Number of Coins for the user
                break
            else:
                print("Please only enter a number between 100 and 800")
        except ValueError:
            print("Please enter a valid integer.")  # to only enter a valid answer


# Game play loop starts here with player one
while total_c > 0:  # following the rules of the game
    try:
        player_one = int(input("Player One (•̀o•́)ง, are you ready? Enter how many coins you will take: "))
        if player_one > 0 and player_one <= total_c and int(player_one**0.5)**2 == player_one:
            # to make sure it's a non-zero square number
            # to check if input is less than/equal to total''the total cannot be negative''
            total_c = total_c - player_one  # subtract the input from the total of coins
            print("Now we have", total_c, "coins")
            if total_c == 0:  # winning condition
                print("★GAME OVER★ player one wins ↖(^▽^)↗ Congratulations!, Good Game player two (● ︵ ●)")
                break  # there is a winner and the game ended
        else:
            print("Please follow the game rules ಠ_ಠ and choose a valid answer")
            continue
    except ValueError:
        print("Please enter a valid integer.")   # to only enter a valid answer
        continue
# loop for player two
    while True:
        try:
            player_two = int(input("Player two (•̀o•́)ง, it’s your turn now! Enter how many coins you will take: "))
            if player_two > 0 and player_two <= total_c and int(player_two**0.5)**2 == player_two:
                # to make sure it's a non-zero square number
                # added condition to check if input is less than/equal to total''the total cannot be negative''
                total_c = total_c - player_two  # subtract the input from the total of coins
                print("Now we have", total_c, "coins")
                if total_c == 0:  # winning condition
                    print("★GAME OVER★ player two wins ↖(^▽^)↗ Congratulations!, Good Game player one (● ︵ ●)")
                    break  # there is a winner and the game ended
                break  # exit the loop for player two if input is valid
            else:
                print("Please follow the game rules ಠ_ಠ and choose a valid answer")
        except ValueError:
            print("Please enter a valid integer.")  # to only enter a valid answer
