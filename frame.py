import cv2

# Opens the Video file
cap = cv2.VideoCapture("video path")

i = 0
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break
# here is the name of frame which this code will write 
    cv2.imwrite('kang' + str(i) + '.jpg', frame)

    i += 1
    if i == 10:
        break

cap.release()
cv2.destroyAllWindows()

# it will return only 10 frames as we have give here a condition 