import cv2
import numpy as np

path_image = 'img1.jpg'
image = cv2.imread(path_image)

if image is None:
    print("Imagem não encontrada!")
else:
    image_matrice = np.array(image)

print(image_matrice[0][0])