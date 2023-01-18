A simple python script that allows the user to play rock paper scissors with the computer using user's camera as input for user decision.

# Project Description

You are stranded on an island with no friends. Assuming you had friends back home, you start to feel a bit lonely. You seem to have all your essential needs covered except now you are bored. You have a laptop though, with solar-panels to power up the laptop. Since you are a newbie to python programming, you decide to develop a very simple game: Rock, Paper, Scissors. 

skills used: python

## This is part of AiCore Projects

I describe the challenges and hurdles that I have overcome throughout the process of developing this script. 

## Milestone 1: Set up the environment

- Q: What have you built? 
- A: Set up Github Repository. New directories. 

## Milestone 2: Create the computer vision system

- Q: What technologies have you used? 
- A: VS Code, MiniConda and Git. Command line - using terminal commands to manipulate files and directories. Use Teachable-Machine to generate a model for Rock, Paper, Scissors. Downloaded files onto home directory.

## Milestone 3: Install the dependencies

- Q: What technologies have you used? 
- A: Virtual Environment set up named as my_env. Installed pip and other libraries within conda. 

## Milestone 4: Create the computer vision system

- Q: What did you achieve?
- A: Wrote a simple script to ask for user's input for rock paper scissors game. A random choice selector for the 'computer'. Wrapped the relevant functions into one over-arching function called play().

## Milestone 5: Use the camera to play Rock-Paper-Scissors

- Q: What did you achieve?
- A: Created two classes: RPS and Timer. Each one has methods specific for its class. Helps clean up the code. Now, including the magic cell lines, comments and separator lines, the whole script is 38 lines only (as opposed to 250+ lines if all written in one file). Used numpy array methods to find the index of the maximum value, which was used to return the user choice. I introduced a modfiable countdown timer that will show up in the terminal. When the timer reaches 0, the camera will activate to take a snapshot of the player to obtain user_choice. There is a scoreboard that is printed after each round. When either party reaches the win condition (set by the user at the beginning), the game ends. Prompts to replay the game if the player wishes to do so. 

```python
"""
# %%
# Computer Vision Project
# Import modules/classes required
from rps_class import RPS
from timer_class import Timer
# %%
# Initiate an instance of the RPS class
rps = RPS()
# %%
def play():
    options = ['Rock', 'Paper', 'Scissors']
    user_wins = 0
    computer_wins = 0
    win_condition = int(rps.get_win_condition())  #How many wins needed to win the game.
    t = Timer()
    seconds = t.set_time()
    q = True
    while q == True:
        t.countdown(seconds)
        user_choice= rps.get_user_choice(seconds)
        computer_choice= rps.get_computer_choice(options)
        result = rps.get_winner(computer_choice, user_choice)
        computer_wins = result[0]
        user_wins = result[1]
        print(f"Score: Computer vs Player. \n\t\t{computer_wins}:{user_wins}")
        if computer_wins == win_condition or user_wins == win_condition:
            q = False
            
    if user_wins == win_condition:
        print("You won the game!")
        
    elif computer_wins == win_condition:
        print("You lost the game!")
    
    if input("Press c to continue?") == 'c':
        play()
    else:
        pass
# %%
play()
"""
```
## Conclusion - 

Though the model data struggles to differentiate scissors from rock (almost always leaning towards rock), the script does work as intended. Other additional features this code could benefit from involve, having the camera always on and then the countdown to appear on screen. Right now, my camera capture function is within the get user_choice function, which terminates after 3 seconds from the time it is initiated. I have tried my best to prevent some of the warning messages appearing but others I could not find the way to hide them.

