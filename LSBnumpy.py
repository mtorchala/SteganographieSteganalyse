from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#im = Image.open("katze.jpg")
im = Image.open(r"C:\Users\Mo\PycharmProjects\untitled2\venv\katze.jpg")
width,height = im.size;
pixelMap = im.load();
text = "Read the elements of a using this index order, and place the elements into the reshaped array using this index order. ‘C’ means to read / write the elements using C-like index order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to read / write the elements using Fortran-like index order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of indexing. ‘A’ means to read / write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise." # geheime Nachricht

asciiText = []
asciiTextBIN = []
for y in range(len(text)):
    asciiText.append(ord(text[y]))              # Text in Binärform umwandeln
    asciiTextBIN.append(bin(ord(text[y]))[2:])

#print("ASCII Text: " + str(asciiText))

for k in range(len(asciiTextBIN)):
    string = ""
    for z in range(8 - len(asciiTextBIN[k])):
        string += "0"
        asciiTextBIN[k] = string + asciiTextBIN[k]

#print("ASCII Text BINÄR: " + str(asciiTextBIN))

asciiString = ""
for string in range(len(asciiTextBIN)):
    asciiString += asciiTextBIN[string];

#print(asciiString)




#convert image to numpy array
numpyImage = np.array(im)
#convert image to greyscale
gray = np.mean(im, -1).astype(int)

#create a new list that acts as a mask to encode the information
mask = [int(i) for i in str(int(asciiString))]
maskAnd = [i+254 for i in mask] #binary 11111110
maskOr = mask
#reshape the image from 2 dimensional [width,height] to one dimensional [width*height]
flatImage = gray.flatten()
fltcp = flatImage
#encode the information using binary operations
#overwrite the zeros
flatImage[0:maskAnd.__len__()] = np.bitwise_and(flatImage[0:maskAnd.__len__()],maskAnd)
#overwrite the ones
flatImage[0:maskOr.__len__()] = np.bitwise_or(flatImage[0:maskOr.__len__()],maskOr)

result = flatImage.reshape(gray.shape)
result = result.astype(np.uint8)
plt.imshow(result-gray)

finalImage = Image.fromarray(result)

finalImage.save("katzesteg.png","PNG", quality=100, optimize=False, progressive=False)