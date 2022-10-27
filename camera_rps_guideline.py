import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5', compile=False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
       
    while True: 
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

    x=prediction[0]
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


def countdown(seconds=3):  
    time_finish = int(time.time()) + seconds
    while int(time.time()) < int(time_finish):
        time_now = int(time.time())
        count_down = time_finish - time_now
        print(int(count_down))
    

get_prediction()
countdown(3)


