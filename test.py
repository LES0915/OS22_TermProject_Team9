import cv2

print('Enter the named')
a = input()

cap = cv2.VideoCapture(0)
if cap.isOpened():

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('camera', frame)

            if cv2.waitKey(1) != -1:
                cv2.imwrite('knowns/{}.jpg'.format(a), frame)
                break

        else:
            print('no frame')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()