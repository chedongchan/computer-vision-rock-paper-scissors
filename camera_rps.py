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

# All files and scripts updated, documented and uploaded to GitHub https://github.com/chedongchan/computer-vision-rock-paper-scissors repo.
