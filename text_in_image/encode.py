from PIL import Image
import sys


def text_to_ascii(text):
    result = []
    for i in range(len(text)):
        result.append(ord(text[i]))
    result.append(3)  # end of text ascii number
    return result


def text_to_binary(text):
    ascii_array = text_to_ascii(text)
    result = []
    for element in ascii_array:
        # slice of first two elements '0b1111' -> '1111'
        binary_element = bin(element)[2:]

        # [2:] Slice off the  first to chars
        result.append(format(element, "#010b")[2:])
    return result


img = Image.open("katze_gs.png")
width, height = img.size
pixel_map = img.load()
text = "Jules rulez!"

ascii_list = text_to_ascii(text)
binary_list = text_to_binary(text)

# Concat all binary chars to one long string
# in order to iterate over it char by char and not element by element
binary_string = "".join(binary_list)

# print(ascii_list)
# print(binary_list)
# print(binary_string)

pixel_max = width * height
current_pixel = 1
binary_string_index = 0  # Index of current bit to insert
encoded_img = Image.new(img.mode, img.size)
print("Number of pixel:", str(pixel_max))
for x in range(width):
    for y in range(height):
        print("\rCurrent Pixel:\t", current_pixel, end="")

        pixel = pixel_map[x, y]  # Pixel has a value between 0 and 254
        if binary_string_index < len(binary_string):
            # convert value from pixel to binary with 10 bit and add text bit
            encoded_pixel = (
                format(pixel, "010b")[2:] + binary_string[binary_string_index]
            )
            encoded_img.putpixel((x, y), (int(encoded_pixel, 2)))
            binary_string_index += 1
        else:
            encoded_img.putpixel((x, y), pixel)
        current_pixel += 1
print("\n")

encoded_img.save(
    "katze_encoded.png", "PNG", quality=100, optimize=False, progressive=False
)
