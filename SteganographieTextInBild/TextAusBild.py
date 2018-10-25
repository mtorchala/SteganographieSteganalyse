from PIL import Image

im = Image.open("katzesteg.png")
width,height = im.size
pixelMap = im.load()

BIN = []
for i in range(width):
    for j in range(height):
        RGB = pixelMap[i, j]
        print(RGB)
        ROT = RGB[0]
        GRÜN = RGB[1]
        BLAU = RGB[2]
        BIN.append(format(ROT, '#010b')[-1:])
        BIN.append(format(GRÜN, '#010b')[-1:])
        BIN.append(format(BLAU, '#010b')[-1:])

index1 = 0
index2 = len(BIN)
string = ""
for index1 in range(index2):
    string += BIN[index1]

print(string)
stringneu = ""
#for i in range (round(len(string)/8)):
for i in range (200):
    ind1= i*8
    ind2= (i+1)*8
    s = string[ind1:ind2]
    i = int(s,2)
    stringneu += chr(i)


print(stringneu)

