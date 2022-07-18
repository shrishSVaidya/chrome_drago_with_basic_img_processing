import cv2
import numpy as np
import pyautogui

cap=cv2.VideoCapture(0)
pyautogui.PAUSE=0.007                                             


while True:

    rt, frame= cap.read()
    height, width=frame.shape[0], frame.shape[1]
    rect_top_left=[int(width*0.05), int(height*0.2)]
    rect_bottom_right=[int(width*0.45), int(height*0.75)]
    cv2.rectangle(frame, (rect_top_left[0], rect_top_left[1]), (rect_bottom_right[0], rect_bottom_right[1]), (0, 255, 0), 2)
    
    hand= frame[rect_top_left[1]:rect_bottom_right[1], rect_top_left[0]:rect_bottom_right[0]].copy()

    hsvim = cv2.cvtColor(hand, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvim, np.array([2,0,0]), np.array([20, 255, 255]))
 
    whitey = np.sum(mask)

    # print(whitey/(hand.shape[0]*hand.shape[1]))
    if(whitey/(hand.shape[0]*hand.shape[1])  > 110):
        print("yes", whitey/(hand.shape[0]*hand.shape[1]))
        # pyautogui.press(' ')

    cv2.imshow("Output", frame)
    cv2.imshow("hand", mask)

    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows(0)