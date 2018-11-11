from PIL import Image
import numpy as np

# Splits List in to List of chunks with same size
# [1,2,3,4] with size 2 -> [[1,2], [3,4]]
def into_chunks(obj, size):
    result = []
    for i in range(0, len(obj), size):
        if i + size < len(obj):
            result.append(obj[i : i + size])
        else:
            result.append(obj[i : len(obj)])
    return result


# Converts list of binaries to list of ascii numbers
def binary_to_ascii(array):
    result = []
    for el in array:
        ascii_number = int(el, 2)
        if ascii_number == 3:
            break
        result.append(ascii_number)
    return result


# Converts list of ascii numbers into a string
def ascii_list_to_text(array):
    result = ""
    for el in array:
        result += chr(el)
    return result


img = Image.open("katze_encoded.png")
width, height = img.size
pixel_array = np.array(img).flatten()

number_of_pixel = width * height  # total number of pixels
binary_string = ""
for i in range(0, number_of_pixel, 11):
    # Pixel has a value between 0 and 254
    pixel = pixel_array[i]

    # convert pixel to binary and take last bit
    binary_string += format(pixel, "b")[-1]

# Split binary string
binary_list = into_chunks(binary_string, 8)
# Turn it to ascii
ascii_list = binary_to_ascii(binary_list)
# Convert ascii to chars
text = ascii_list_to_text(ascii_list)

print(text)
