import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",(20,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Mercury",(120,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Venus",(200,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Earth",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Mars",(400,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Jupiter",(500,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Saturn",(800,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Uranus",(1000,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )
cv2.putText(img,
            "Neptune",(1100,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255)
            )







cv2.imshow("output",img)
cv2.waitKey(0)
