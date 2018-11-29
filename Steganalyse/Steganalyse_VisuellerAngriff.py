from PIL import Image

def binary_combinations(LSBcount):
    list_binary_combinations = []
    binary = 0

    for i in range(2**LSBcount):
        s = ""
        binary_combination = format(binary, "b")[-LSBcount:]
        for n in range(LSBcount-len(binary_combination)):
            s = s + "0"
        list_binary_combinations.append(s+binary_combination)
        binary+=1

    return list_binary_combinations

img = Image.open("katze_encoded.png")
width, height = img.size
pixel_map = img.load()

total_pixel = width * height  # total number of pixels
encoded_img = Image.new(img.mode, img.size)
LSBcount = 1
list_binary_combination = binary_combinations(LSBcount)
for y in range(height):
    for x in range(width):
        pixel = pixel_map[x, y]
        formattedpixel = format(pixel, "b")
        s = ""
        for n in range(8-len(formattedpixel)):
            s = s + "0"

        full_binary = s + formattedpixel
        binary_LSB = full_binary[-LSBcount:]
        for m in range(len(list_binary_combination)):
            if list_binary_combination[m] == binary_LSB:
                encoded_img.putpixel((x,y),int((254/LSBcount**2 -1) * m))

encoded_img.save("katze_stega.png", "PNG", quality=100, optimize=False)


