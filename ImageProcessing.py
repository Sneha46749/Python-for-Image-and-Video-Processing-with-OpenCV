import cv2

img = cv2.imread("Galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)  #To check image resolution
print(img.ndim)   #To check the dimension of image

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("GalaxyResized.jpg",resized_image)
cv2.waitKey(10000) #Sets the time in milliseconds after which the window will close
cv2.destroyAllWindows()