import cv2
import numpy as np
from scipy.spatial import distance

#Vnos za stevilo centrov
print("Vpisi Stevilo centrov")
x = int(input())
print(x)

#Preberemo in prikazemo demo sliko
img = cv2.imread("lenna.png", 1)
cv2.imshow("Lenna", img)

#Naso drugo sliko priredimo prvi sliki
original2 = img

#Komponenta priredimo velikost glede na shape slike
height = img.shape[0]
width = img.shape[1]

#Napolnimo naše polje x*3 s vrednosti med 0 in 255
centers=np.random.randint(255, size=(x,3))
#Izpisemo vse centre
for c in centers:
        print(c)
#Matrika za najblizje distance, nastavimo ji enako velikost, kot velikost slike
closedist = [[0 for x in range(height)] for y in range(width)]

#Minimumu nastavimo na nekaj vecjega, tako da ga ze prva vrednost zamenja
minimum = 10000

#Zanka ki gre skozi sliko in za vsak pixel izracuna kateri center mu je najblizji (centru priredimo vrednost i)
#Za evklido razdaljo sem vzel iz knjiznjice distance.euclidan
for x in range(0, height):
    for y in range(0, width):
        minimum = 10000
        i = 0
        for c in centers:
            dist = distance.euclidean(c, img[x, y])
            if (dist < minimum):
                minimum = dist
                closedist[x][y] = i
            i += 1
            # print(distance.euclidean(c, img[x, y]))

#Imamo 3 vsote(za vsako barvo 1 vsota, katerim priredimo začetno vrednost 0, prav tako i
sum = 0
sum2 = 0
sum3 = 0
i = 0
# Gremo skozi vse centre in za vsak pixel v sliki ki ustreza centru sestevamo barve, nato ko preletimo sliko, zracunamo
# povprecja in nato to barvo priredimo vsem tem pixlom v sliki
# Postopek ponovimo za vsak center, na koncu zanke se nastavijo vsote na 0, i(ki je misljen kot stevec za centre, pa
# se poveca za 1
for c in centers:
    stevec = 0
    for x in range(0, height):
        for y in range(0, width):
            if (closedist[x][y] == i):
                sum = sum + img[x, y, 0]
                sum2 = sum2 + img[x, y, 1]
                sum3 = sum3 + img[x, y, 2]
                stevec += 1
    print("Vsote : ", sum, sum2, sum3)
    print("Counter : ", stevec)
    try:
        avg1 = sum / stevec
        avg2 = sum2 / stevec
        avg3 = sum3 / stevec
        print("Povprecja : ", avg1, avg2, avg3)
        for x in range(0, height):
            for y in range(0, width):
                if (closedist[x][y] == i):
                    original2[x, y, 0] = avg1
                    original2[x, y, 1] = avg2
                    original2[x, y, 2] = avg3
    except:
        print("Obstaja center ki ni najblizji nobenemu pixlu")
    sum = 0
    sum2 = 0
    sum3 = 0
    i += 1
cv2.imshow("Rezultat", original2)

cv2.waitKey()
cv2.destroyAllWindows()
