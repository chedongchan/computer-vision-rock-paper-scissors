# %% 
# Import modules
import cv2
from keras.models import load_model
import numpy as np
import time
import random


class RPS():
    def __init__(self):
        self.cp = 0    # computer points
        self.up = 0    # user points

# Randomly selects one option for the game. 
    def get_computer_choice(self, options):    
        computer_choice = random.choice(options)  
        print(f'Computer chose {computer_choice}.')
        return computer_choice

# Asks for user input for rock,paper or scissors

    def get_user_choice(self, seconds):
        user_choice = self.get_prediction(seconds)
        print(user_choice)
        return user_choice

    def get_prediction(self, seconds):
        model = load_model('keras_model.h5', compile=False)
        end_time = time.time() + int(seconds)
        while end_time > time.time(): 
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data , verbose=0)
            cv2.imshow('frame', frame)
            
            
            # Press q to close the window
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()


        x = prediction[0]
        index = np.argmax(x)
        if index == 0:
            return 'You chose rock'
        elif index ==1:
            return 'You chose paper'
        elif index ==2:
            return 'You chose scissors'
        else: 
            return 'You chose nothing'

# The below lines are my initial attempts to find the max value and print out the user's choice.
#   x[0] = rock  x[1] = paper   x[2] = scissors   x[3] = nothing
    # if x[0] > x[1] and x[0] > x[2] and x[0] > x[3]:
    #     return 'You chose rock'
    # elif x[1] > x[0] and x[1] > x[2] and x[1] > x[3]:
    #     return 'You chose paper'
    # elif x[2] > x[0] and x[2] > x[1] and x[2] > x[3]:
    #     return 'You chose scissors'
    # else: 
    #     return 'You chose nothing'

# Conditionals set to print out the outcome

    def get_winner(self,computer_choice, user_choice):
        
        x= True
        while x == True:
            if computer_choice == 'Rock':
                if user_choice =='You chose rock':
                    print("You draw")
                elif user_choice =='You chose scissors':
                    print("You lose")
                    self.cp +=1
                elif user_choice == 'You chose paper':
                    print("You win!")
                    self.up +=1

                x = False

            elif computer_choice == 'Paper':
                if user_choice =='You chose rock':
                    print("You lose")
                    self.cp +=1
                elif user_choice =='You chose scissors':
                    print("You win!")
                    self.up +=1
                elif user_choice == 'You chose paper':
                    print("You draw")
                x = False
            
            elif computer_choice == 'Scissors':
                if user_choice =='You chose rock':
                    print("You win!")
                    self.up +=1
                elif user_choice =='You chose scissors':
                    print("You draw")
                elif user_choice == 'You chose paper':
                    print("You lose")
                    self.cp +=1
                x = False
            else:
                x = False
        
        return self.cp, self.up

# Ask for win condition

    def get_win_condition(self):
        win_condition = input("How many wins to victory?")
        return win_condition
