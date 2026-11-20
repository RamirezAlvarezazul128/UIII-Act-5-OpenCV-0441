import cv2
## Ramirez Azul NC 0441
# Leer la imagen desde el archivo
image = cv2.imread('taehbb.jpg')
# Mostrar la imagen en una ventana
cv2.imshow('Image', image)
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Guardar la imagen resultante
cv2.imwrite('gray_image.jpg', gray_image)


# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Redimensionar a 300x200 píxeles
resized_image = cv2.resize(image, (300, 200))
# Guardar la imagen redimensionada
cv2.imwrite('resized_image.jpg', resized_image)


# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Obtener alto y ancho de la imagen
(h, w) = image.shape[:2]
# Definir el centro de la imagen
center = (w // 2, h // 2)
# Matriz de rotación
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Aplicar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h))
# Guardar la imagen rotada
cv2.imwrite('rotated_image.jpg', rotated_image)


# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Aplicar desenfoque gaussiano
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# Guardar la imagen desenfocada
cv2.imwrite('blurred_image.jpg', blurred_image)


# Cargar la imagen
image= cv2.imread('taehbb.jpg')
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Aplicar detector de bordes Canny
edges = cv2.Canny(gray_image, 100, 200)
# Guardar la imagen de bordes
cv2.imwrite('edges.jpg', edges)



# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Dibujar un rectángulo
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
# Agregar texto a la imagen
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Guardar la imagen resultante
cv2.imwrite('output_image.jpg', image)


# Cargar la imagen en escala de grises
image = cv2.imread('taehbb.jpg', 0)
# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Guardar la imagen binarizada
cv2.imwrite('threshold_image.jpg', thresh_image)



# Cargar la imagen
image = cv2.imread('taehbb.jpg')
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detectar bordes
edges = cv2.Canny(gray_image, 100, 200)
# Encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar los contornos sobre la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Guardar la imagen con los contornos dibujados
cv2.imwrite('contours_image.jpg', image)
print("Ramirez Azul NC 0441")



import cv2

print("Ramirez Azul NC 0441")

# 1. Imagen original
image = cv2.imread('taehbb.jpg')
cv2.imshow('1. Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray_image)
cv2.imshow('2. Escala de grises', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Redimensionar
resized_image = cv2.resize(image, (300, 200))
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imshow('3. Redimensionada', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Rotar 90 grados
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))
cv2.imwrite('rotated_image.jpg', rotated_image)
cv2.imshow('4. Rotada', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Desenfoque Gaussiano
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('blurred_image.jpg', blurred_image)
cv2.imshow('5. Desenfoque', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Detección de bordes (Canny)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imwrite('edges.jpg', edges)
cv2.imshow('6. Bordes Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Dibujar rectángulo y texto (se hace sobre una copia para no dañar la original)
img_shapes = image.copy()
cv2.rectangle(img_shapes, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.putText(img_shapes, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite('output_image.jpg', img_shapes)
cv2.imshow('7. Figuras y texto', img_shapes)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Umbralización binaria
_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold_image.jpg', thresh_image)
cv2.imshow('8. Umbralizacion', thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Detección de contornos (se dibuja sobre otra copia de la original)
img_contours = image.copy()
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
cv2.imwrite('contours_image.jpg', img_contours)
cv2.imshow('9. Contornos', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()