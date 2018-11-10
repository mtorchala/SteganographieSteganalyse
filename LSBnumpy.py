from PIL import Image

# import matplotlib.pyplot as plt
import numpy as np

# im = Image.open("katze.jpg")
im = Image.open("text_in_image/katze_gs.png")


width, height = im.size
pixelMap = im.load()
text = "abc"

asciiText = []
asciiTextBIN = []
for y in range(len(text)):
    asciiText.append(ord(text[y]))  # Text in Binärform umwandeln
    asciiTextBIN.append(bin(ord(text[y]))[2:])

# print("ASCII Text: " + str(asciiText))

for k in range(len(asciiTextBIN)):
    string = ""
    for z in range(8 - len(asciiTextBIN[k])):
        string += "0"
        asciiTextBIN[k] = string + asciiTextBIN[k]

# print("ASCII Text BINÄR: " + str(asciiTextBIN))

asciiString = ""
for string in range(len(asciiTextBIN)):
    asciiString += asciiTextBIN[string]

# print(asciiString)


# convert image to numpy array
numpyImage = np.array(im)

# create a new list that acts as a mask to encode the information
mask = [int(i) for i in str((asciiString))]

# print (mask)
maskAnd = [i + 254 for i in mask]  # binary 11111110
maskOr = mask
# reshape the image from 2 dimensional [width,height] to one dimensional [width*height]
flatImage = numpyImage.flatten()

# encode the information using binary operations
# overwrite the zeros
flatImage[0 : maskAnd.__len__()] = np.bitwise_and(
    flatImage[0 : maskAnd.__len__()], maskAnd
)
# overwrite the ones
flatImage[0 : maskOr.__len__()] = np.bitwise_or(flatImage[0 : maskOr.__len__()], maskOr)

result = flatImage.reshape(numpyImage.shape)
result = result.astype(np.uint8)
# plt.imshow(result-numpyImage)

finalImage = Image.fromarray(result)

finalImage.save(
    "text_in_image/katze_encoded.png",
    "PNG",
    quality=100,
    optimize=False,
    progressive=False,
)
