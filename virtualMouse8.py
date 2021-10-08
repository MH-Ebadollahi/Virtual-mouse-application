import cv2
import numpy as np
import mediapipe as mp
from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()


def handDetectionRight(frame, mouseX, mouseY):
    # ############ initial defines ############ #
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                          max_num_hands=1,
                          min_detection_confidence=0.7,
                          min_tracking_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils
    # ###### convert BGR 2 RGB because the process method works through RGB ##### #
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detect = hands.process(frameRGB)
    # ############# hand detection ############# #
    classification = str(detect.multi_handedness)
    if 'Right' in classification:
        whichHand = 'Hand : Right'
    elif 'Left' in classification:
        whichHand = 'Hand : Left'
    else:
        whichHand = 'Hand : None'
    cv2.rectangle(frame, (3980, 10), (5100, 270), (0, 170, 240), cv2.FILLED)
    cv2.putText(frame, whichHand, (4000, 170), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
    ###############################################
    if detect.multi_hand_landmarks and 'Right' in classification:
        for handlms in detect.multi_hand_landmarks:
            # draw hand landmarks and connections
            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)
            # register the height , wight, layer of the frame
            h, w, c = frame.shape
            # print(frame.shape)
            # print(detect.multi_hand_landmarks)

            # ######## Index finger ######## #
            index_Tip = handlms.landmark[8]
            index_Dip = handlms.landmark[7]
            index_Tip_y = int(index_Tip.y * h)
            index_Dip_y = int(index_Dip.y * h)
            if index_Tip_y > index_Dip_y:
                mouse.click(Button.left, 1)
                cv2.rectangle(frame, (3980, 300), (5100, 560), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Left Click", (4150, 480),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ####### Pinky finger ####### #
            pinky_Tip = handlms.landmark[20]
            pinky_Dip = handlms.landmark[19]
            pinky_Tip_y = int(pinky_Tip.y * h)
            pinky_Dip_y = int(pinky_Dip.y * h)
            if pinky_Tip_y > pinky_Dip_y:
                mouse.click(Button.right, 1)
                cv2.rectangle(frame, (3980, 590), (5100, 850), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Right Click", (4080, 770),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ####### Right Thumb ####### #
            thumb_Tip = handlms.landmark[4]
            index_mcp = handlms.landmark[5]
            thumb_Tip_x = int(thumb_Tip.x * w)
            index_mcp_x = int(index_mcp.x * w)
            if thumb_Tip_x > index_mcp_x:
                mouse.click(Button.left, 2)
                cv2.rectangle(frame, (3980, 880), (5100, 1140), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Double Click", (4000, 1060),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ############################# #
            for iD, lm in enumerate(handlms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                xCalibration = np.interp(cx, [1000, 4300], [0, mouseX])   # Ex: [0-1536] x-size of screen
                yCalibration = np.interp(cy, [1200, 2400], [0, mouseY])   # Ex: [0-863]  y-size of screen
                if iD == 9:
                    xCalibration9 = xCalibration
                    yCalibration9 = yCalibration
                    mouse.position = (xCalibration9, yCalibration9)
                    cv2.rectangle(frame, (900, 1100), (4400, 2500), (255, 0, 0), 8)
                    cv2.circle(frame, (cx, cy), 35, (255, 0, 255), cv2.FILLED)
                    # print(cx, cy)

    return frame


def handDetectionLeft(frame, mouseX, mouseY):
    # ############ initial defines ############ #
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                          max_num_hands=1,
                          min_detection_confidence=0.7,
                          min_tracking_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils
    # ###### convert BGR 2 RGB because the process method works through RGB ##### #
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detect = hands.process(frameRGB)
    # ############# hand detection ############# #
    classification = str(detect.multi_handedness)
    if 'Right' in classification:
        whichHand = 'Hand : Right'
    elif 'Left' in classification:
        whichHand = 'Hand : Left'
    else:
        whichHand = 'Hand : None'
    cv2.rectangle(frame, (3980, 10), (5100, 270), (0, 170, 240), cv2.FILLED)
    cv2.putText(frame, whichHand, (4000, 170), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
    ###############################################
    if detect.multi_hand_landmarks and 'Left' in classification:
        for handlms in detect.multi_hand_landmarks:
            # draw hand landmarks and connections
            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)
            # register the height , wight, layer of the frame
            h, w, c = frame.shape
            # print(frame.shape)
            # print(detect.multi_hand_landmarks)

            # ######## Index finger ######## #
            index_Tip = handlms.landmark[8]
            index_Dip = handlms.landmark[7]
            index_Tip_y = int(index_Tip.y * h)
            index_Dip_y = int(index_Dip.y * h)
            if index_Tip_y > index_Dip_y:
                mouse.click(Button.left, 1)
                cv2.rectangle(frame, (3980, 300), (5100, 560), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Left Click", (4150, 480),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ####### Pinky finger ####### #
            pinky_Tip = handlms.landmark[20]
            pinky_Dip = handlms.landmark[19]
            pinky_Tip_y = int(pinky_Tip.y * h)
            pinky_Dip_y = int(pinky_Dip.y * h)
            if pinky_Tip_y > pinky_Dip_y:
                mouse.click(Button.right, 1)
                cv2.rectangle(frame, (3980, 590), (5100, 850), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Right Click", (4080, 770),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ####### Left Thumb ####### #
            thumb_Tip = handlms.landmark[4]
            index_mcp = handlms.landmark[5]
            thumb_Tip_x = int(thumb_Tip.x * w)
            index_mcp_x = int(index_mcp.x * w)
            if thumb_Tip_x < index_mcp_x:
                mouse.click(Button.left, 2)
                cv2.rectangle(frame, (3980, 880), (5100, 1140), (0, 170, 240), cv2.FILLED)
                cv2.putText(frame, "Double Click", (4000, 1060),
                            cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 12)
                sleep(0.3)
            # ############################# #
            for iD, lm in enumerate(handlms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                xCalibration = np.interp(cx, [1000, 4300], [0, mouseX])  # Ex: [0-1536] x-size of screen
                yCalibration = np.interp(cy, [1200, 2400], [0, mouseY])  # Ex: [0-863]  y-size of screen
                if iD == 9:
                    xCalibration9 = xCalibration
                    yCalibration9 = yCalibration
                    mouse.position = (xCalibration9, yCalibration9)
                    cv2.rectangle(frame, (900, 1100), (4400, 2500), (255, 0, 0), 8)
                    cv2.circle(frame, (cx, cy), 35, (255, 0, 255), cv2.FILLED)
                    # print(cx, cy)

    return frame


def resizeFrame(frame, wight, height):
    reFlipFrame = cv2.flip(frame, 1)
    resizedFrame = cv2.resize(reFlipFrame, (int(8 * wight), int(8 * height)))  # frame is resized
    return resizedFrame


def screenCalibration():
    print("""
    welcome to the Virtual Mouse Application
    developed by Mohammad Hossein Ebadollahi
          published on September 2021
    """)
    input("""
    To measure the size of your screen for calibrating the application,
    and determination of the virtual mouse cursor's action area.
    Please put and hold the cursor on the down-Right corner( __| )
    of your screen, then press ' C ' key on your keyboard for confirmation.
    >> """)
    mouseX, mouseY = mouse.position
    print("""
    your screen size is: x = {} , y = {}""".format(mouseX, mouseY))
    print("\nCalibration Done")

    return mouseX, mouseY
