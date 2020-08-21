import cv2, time

video = cv2.VideoCapture(0)  #Here argument is the image captured by webcam
a = 1

while True:
    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("CapturedImg", frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)  #Prints number of frames/iterations
video.release()
cv2.destroyAllWindows