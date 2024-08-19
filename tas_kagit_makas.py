# -*- coding: utf-8 -*-

import random

def tas_kagit_makas_MUHAMMET_ZİYALI():
    print(
    """Hello and welcome to the Rock, Paper, Scissors game!
In this game, the player who wins two rounds wins.
Please make your choice: Rock, Paper, or Scissors. 
If you wish to exit the game, simply use the 'exit' command.
Let’s get started and enjoy the game!
"""
)
    rounds_played=1
    games_played=1
    computer_wins=0
    player_wins=0
    
    choices = ["rock", "paper", "scissors"]
    
    while(True):
        print(f"###### GAME {games_played} ROUND {rounds_played} ! ######")
        
        player_choice=(input("Rock, Paper, Scissors or Exit: ")).lower()
        computer_choice = random.choice(choices)
        
        
        if ((player_choice != "rock") and (player_choice != "paper") 
        and (player_choice != "scissors") 
        and (player_choice != "exit")):
            print(" * Invailed choice! Please try again."  
                  "\n * Either choose Rock, Paper or Scissors! \n")
            continue
       
        if (games_played == 1 and player_choice == "exit"):
            print("* Leaving so quickly? I thought you were up for a real challenge!")
            break
        elif (games_played > 1 and player_choice == "exit"):
            print("* Thank you for playing! We hope you had fun. Come back anytime for another game!")
            break
        
        
        if (player_choice == computer_choice):
            rounds_played+=1
            print(
    f"""
    \n * Computer chose: ## {computer_choice.upper()} ##\n
    \n * It's a tie this round! \n
    \n * Player = {player_wins}, Computer = {computer_wins} \n
    \n---------------------------------------- \n
    """
)         
        elif ((player_choice == "rock" and computer_choice == "scissors") or 
        (player_choice == "scissors" and computer_choice == "paper") or 
        (player_choice == "paper" and computer_choice == "rock")):
            rounds_played+=1
            player_wins+=1
            print(
    f"""
    \n * Computer chose: ## {computer_choice.upper()} ##\n
    \n * You are so lucky! You win this round. \n
    \n * Player = {player_wins}, Computer = {computer_wins} \n
    \n---------------------------------------- \n
    """
)  
        else:
            rounds_played+=1
            computer_wins+=1
            print(
    f"""
    \n * Computer chose: ## {computer_choice.upper()} ##\n
    \n * Hah! You lose this round! \n
    \n * Player = {player_wins}, Computer = {computer_wins} \n
    \n---------------------------------------- \n
    """
)
        if (player_wins == 2 or computer_wins == 2):
            if player_wins == 2:
                print("* You have won the game!")
                replay_choice= (input("Do you want to challenge me again,champion? (Yes or No): ")).lower()
                computer_replay_choice= random.choice(["yes","no"])
            else:
                print("* You have lose the game!")
                replay_choice= (input("Do you want to challenge me again,loser? (Yes or No): ")).lower()
                computer_replay_choice= random.choice(["yes","no"])
            
            if (replay_choice != "yes" and replay_choice != "no"):
                print("\n * There was a mistake in your input. The game has ended. Thanks for playing! \n")
                break
                
            if (computer_replay_choice == "yes" and replay_choice == "yes"):
                print("\n* I want to play again as well! Lets play one more! \n")
                games_played+=1
                rounds_played=1
                player_wins = computer_wins = 0
                continue
            
            elif (replay_choice == "no"):
                print("\n* Oh, calling it quits already? Well, maybe next time! \n")

                break
            elif (computer_replay_choice == "no" ):
                print("\n* Play again? Sorry, I'm taking a break. \n" 
                      "* Computer has left the game.")
                break
            

tas_kagit_makas_MUHAMMET_ZİYALI()

