from PIL import Image
import matplotlib.pyplot as plot

img = Image.open("katze_encoded.png")
img = img.convert('L')
width, height = img.size
pixel_map = img.load()
anzahlpixel = width * height
summepixelanzahl = 0

X = []
Ymanipuliert = []

for pixel_value in range(256):
    count = 0
    for y in range(height):
        for x in range(width):
            if pixel_map[x, y] == pixel_value:
                count += 1
    X.append(pixel_value)
    Ymanipuliert.append(count)
plot.plot(X, Ymanipuliert)

#Mittelwert für manipuliertes Bild bestimmen
for ind in range(len(Ymanipuliert)):
        summepixelanzahl = summepixelanzahl + Ymanipuliert[ind]

mittelwert_manipuliert = summepixelanzahl / len(Ymanipuliert)
print("Mittelwert(manipuliert): " + str(mittelwert_manipuliert))

#Varianz für Originalbild bestimmen
summe_abweichungen_manipuliert = 0;
for ind in range(len(Ymanipuliert)):
        summe_abweichungen_manipuliert = summe_abweichungen_manipuliert + (Ymanipuliert[ind] - mittelwert_manipuliert) ** 2

varianz_manipuliert = summe_abweichungen_manipuliert / len(Ymanipuliert)
print("Varianz(manipuliert): " + str(varianz_manipuliert))
print("Standardabweichung(manipuliert): " + str(varianz_manipuliert**0.5))

img = Image.open("katze_gs.png")
img = img.convert('L')
width, height = img.size
pixel_map = img.load()
anzahlpixel = width * height
summepixelanzahl = 0

X = []
Yoriginal = []

for pixel_value in range(256):
    count = 0
    for y in range(height):
        for x in range(width):
            if pixel_map[x, y] == pixel_value:
                count += 1
    X.append(pixel_value)
    Yoriginal.append(count)

#Mittelwert für Originalbild bestimmen
for ind in range(len(Yoriginal)):
        summepixelanzahl = summepixelanzahl + Yoriginal[ind]

mittelwert_original = summepixelanzahl / len(Yoriginal)
print("Mittelwert(Original): " + str(mittelwert_original))

#Varianz für Originalbild bestimmen
summe_abweichungen_original = 0;
for ind in range(len(Yoriginal)):
        summe_abweichungen_original = summe_abweichungen_original + (Yoriginal[ind] - mittelwert_original) ** 2

varianz_original = summe_abweichungen_original / len(Yoriginal)
print("Varianz(Original): " + str(varianz_original))
print("Standardabweichung(Original): " + str(varianz_original**0.5))
plot.plot(X, Yoriginal, 'C3')

#Subtraktion von Original und manipuliertem Bild im Betrag
Ysubbetrag = []
for ind in range(len(Yoriginal)):
        sub = Yoriginal[ind] - Ymanipuliert[ind]
        sub = pow(sub,2)
        Ysubbetrag.append(sub**0.5)
plot.plot(X,Ysubbetrag,'C7')


plot.xlabel("Pixelwert")
plot.ylabel("Anzahl Pixel")
plot.savefig('histogramm.png',dpi = 100);
plot.show()





