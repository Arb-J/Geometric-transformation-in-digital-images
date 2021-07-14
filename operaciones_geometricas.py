import cv2
import numpy as np
import math

img = cv2.imread('lena.jpg')

# Escalado de la imagen #

img_escala = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
#img_escala = cv2.resize(img, None, fx=0.70, fy=0.70, interpolation=cv2.INTER_CUBIC)

#Si no se indica el tamaño se utilizan los parámetros fx y fy, si el tamaño se 
# establece estos parámetros son calculados a partir de lo que hayamos establecido.

cv2.imshow('Original', img)
cv2.waitKey()

cv2.imshow('Scale', img_escala)
cv2.waitKey()

# Traslacion de la imagen #

M_traslacion = np.float32([[1, 0, 100], [0, 1, 50]])
img_traslacion = cv2.warpAffine(img, M_traslacion, (630 + 100, 630 + 50), None, cv2.INTER_CUBIC)

# El ultimo parametro es para establecer el tamaño de la nueva imagen, teniendo en 
# cuenta que la imagen se desplazara y es por eso que aumenta su tamaño en la misma
# cantidad que el desplazamiento

cv2.imshow('Traslate', img_traslacion)
cv2.waitKey()

# Rotacion de la imagen #

rows, cols = img.shape[:2]
M_rotacion = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
img_rotacion = cv2.warpAffine(img, M_rotacion, (cols, rows), None, cv2.INTER_CUBIC)

#El punto pivote de rotacion es en el centro de la imagen, angulo de 45 grados, escala 1

cv2.imshow('Rotate', img_rotacion)
cv2.waitKey()

# Inclinacion #

rows, cols = img.shape[:2]

# Definimos los angulos de inclinacion

ix = math.tan(20 * math.pi / 180)
iy = math.tan(15 * math.pi / 180)

M_inclinacion = np.float32([[1, ix, 0], [iy, 1, 0]])
img_inclinacion = cv2.warpAffine(img, M_inclinacion, (cols + 230, rows + 230), None, cv2.INTER_CUBIC)

cv2.imshow('Inclinar', img_inclinacion)
cv2.waitKey()

# Perspectiva #

img_persp = cv2.imread('persp.jpg')
rows2, cols2 = img_persp.shape[:2]

pts1 = np.float32([[113, 137], [256, 136], [270, 337], [140, 377]])
pts2 = np.float32([[0,0], [165, 0], [165, 223], [0, 223]])

M_persp = cv2.getPerspectiveTransform(pts1, pts2)
img_persp_f = cv2.warpPerspective(img_persp, M_persp, (165, 223))

cv2.imshow('Perspective', img_persp)
cv2.waitKey()

cv2.imshow('Final Perspective', img_persp_f)
cv2.waitKey()

