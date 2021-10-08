import cv2
import virtualMouse8 as vm

def main():
    video = cv2.VideoCapture(0)
    mouseX, mouseY = vm.screenCalibration()
    chooseHand = input("Please select your hand for controlling (L / R)? ")

    if chooseHand.lower() == "r":
        while True:
            ret, frame = video.read()
            resizedFrame = vm.resizeFrame(frame, 640, 480)
            processedFrame = vm.handDetectionRight(resizedFrame, mouseX, mouseY)
            normalView = cv2.resize(processedFrame, (640, 480))
            cv2.imshow("virtualMouse", normalView)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        video.release()
        cv2.destroyAllWindows()

    elif chooseHand.lower() == "l":
        while True:
            ret, frame = video.read()
            resizedFrame = vm.resizeFrame(frame, 640, 480)
            processedFrame = vm.handDetectionLeft(resizedFrame, mouseX, mouseY)
            normalView = cv2.resize(processedFrame, (640, 480))
            cv2.imshow("virtualMouse", normalView)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        video.release()
        cv2.destroyAllWindows()
    else:
        print("your choice is not acceptable! try it again ")


main()
