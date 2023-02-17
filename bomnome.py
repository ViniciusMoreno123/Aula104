import cv2

img = cv2.imread("poster.jpg")




#posição original
posFoguete = img[120:360,400:500]
img[0:240,500:600] = posFoguete
#Nova posição
textoLegal = "Vento bom aqui em cima"
cv2.putText(img,textoLegal,(20,220),fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.6,color= (120,0,0))
cv2.imshow("Foguete daora", img)
cv2.waitKey(0)

