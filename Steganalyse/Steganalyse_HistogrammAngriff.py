from PIL import Image
import matplotlib.pyplot as plot

img = Image.open("katze_encoded.png")
img = img.convert('L')
width, height = img.size
pixel_map = img.load()

encoded_img = Image.new(img.mode, img.size)
X = []
Y = []
for pixel_value in range(256):
    count = 0
    for y in range(height):
        for x in range(width):
            if pixel_map[x, y] == pixel_value:
                count += 1
    X.append(pixel_value)
    Y.append(count)
plot.plot(X,Y)

img = Image.open("katze_gs.png")
img = img.convert('L')
width, height = img.size
pixel_map = img.load()

encoded_img = Image.new(img.mode, img.size)
X = []
Y = []
for pixel_value in range(256):
    count = 0
    for y in range(height):
        for x in range(width):
            if pixel_map[x, y] == pixel_value:
                count += 1
    X.append(pixel_value)
    Y.append(count)
plot.plot(X,Y,'C3')
plot.xlabel("Pixelwert")
plot.ylabel("Anzahl Pixel")
plot.savefig('histogramm.png',dpi = 100);
plot.show()





