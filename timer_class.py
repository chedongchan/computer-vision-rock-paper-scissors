# %% 
# Import functions 
import cv2
from keras.models import load_model



# Create class Timer. 
# This will contain a method to ask the user how many seconds they want to countdown.
# This will contain a method to countdown based on the input.

class Timer():
    def __init__(self):
        t = 3
        pass
    
    def set_time(self):
        t = input("Please state how many seconds to coundown")
        return t
        
    def countdown(self, t):
        t = int(t)
        print("Show your hand in...")
        while int(t) > 0:
            cv2.waitKey(1000)       #cv2 module required
            print("{}".format(t))
            t -= 1
    
# %%
