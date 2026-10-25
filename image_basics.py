import numpy as np
import cv2
 
img = cv2.imread('data/lucrece.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

dim_y, dim_x, dim_val = img.shape
print("Dimension de l'image : ", dim_y, " ", dim_x, " ", dim_val)

val = img[100, 50]
print("Valeur Pixel en 50 100 : ", val)

img[0:100, 0:100] = (0, 0, 255)

cv2.imshow("Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("imge_avec_carre.jpg", img)