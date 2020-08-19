import cv2
import glob  #Finds the path names of some files given a certain pattern

images=glob.glob("*.jpg")  #Getting relative paths

for image in images:
    img=cv2.imread(image,0)
    resized=cv2.resize(img,(100,100))
    cv2.imshow("Hey",resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("Resized"+image,resized)