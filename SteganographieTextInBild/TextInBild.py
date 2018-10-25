from PIL import Image

im = Image.open("katze.jpg")
width,height = im.size
pixelMap = im.load()
text = "MitSteganographieVerstecktesGeheimnis" # geheime Nachricht

asciiText = []
asciiTextBIN = []
for y in range(len(text)):
    asciiText.append(ord(text[y]))              # Text in Binärform umwandeln
    asciiTextBIN.append(bin(ord(text[y]))[2:])

print("ASCII Text: " + str(asciiText))

for k in range(len(asciiTextBIN)):
    string = ""
    for z in range(8 - len(asciiTextBIN[k])):
        string += "0"
        asciiTextBIN[k] = string + asciiTextBIN[k]

print("ASCII Text BINÄR: " + str(asciiTextBIN))

asciiString = ""
for string in range(len(asciiTextBIN)):
    asciiString += asciiTextBIN[string]

print(asciiString)
stringindex = 0
img = Image.new(im.mode,im.size)
for i in range(width):
    for j in range(height):
        RGB = pixelMap[i, j]
        print(RGB)
        if(stringindex < len(asciiString)):
            ROT = RGB[0]
            GRÜN = RGB[1]
            BLAU = RGB[2]
            ROTbin = format(ROT, '#010b')[2:9]+asciiString[stringindex]           # Binärform in RGB-Werte integrieren
            if (stringindex +1) < len(asciiString):
                GRÜNbin = format(GRÜN, '#010b')[2:9]+asciiString[stringindex+1]
            if (stringindex + 2) < len(asciiString):
                BLAUbin = format(BLAU, '#010b')[2:9]+asciiString[stringindex+2]
            print(ROTbin)
            print(GRÜNbin)
            print(BLAUbin)
            print("")
            img.putpixel((i,j),(int(ROTbin,2),int(GRÜNbin,2),int(BLAUbin,2)))
            stringindex = stringindex +3
        else:
            img.putpixel((i,j),RGB)                                              # Wenn der geheime Text verarbeitet wurde, werden die originalen Pixel des Bilds verwendet

img.save("katzesteg.png","PNG", quality=100, optimize=False, progressive=False)
