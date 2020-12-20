import cv2

img = cv2.imread('toy4.jpeg')
img = cv2.resize(img, (200, 200))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
blue_mask = cv2.inRange(hsv, (110, 50, 50) , (130, 255, 255))
orange_mask =cv2.inRange(hsv, (5, 50, 50), (15, 255, 255))
red_mask =cv2.inRange(hsv, (170, 120, 70), (180, 255, 255))
green_mask =cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))
lightblue_mask =cv2.inRange(hsv, (80, 120, 70), (95, 255, 255))
cv2.imshow('image', img)
cv2.imshow('Blue color', blue_mask)
cv2.imshow('Orenge color', orange_mask)
cv2.imshow('Red color', red_mask)
cv2.imshow('Green color', green_mask)
cv2.imshow('Light blue color', lightblue_mask)
while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break
cv2.destroyAllWindows()