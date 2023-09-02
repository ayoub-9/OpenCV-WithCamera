import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       #you can replce gray to frame to open camera with colors
       cv2.imshow('frame', gray)

       #q or Q for closing app window
       if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
       break   

cap.release()
cv2.destroyAllWindows()    