from PIL import Image
import numpy as np
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
        result.append(format(element, "08b"))
    return result


img = Image.open("katze_gs.png")
width, height = img.size
pixel_array = np.array(img).flatten()
# text = "IT-Sicherheit ist mein Lieblingsfach! <3"
# text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.   Duis autem vel eum iriure dolor in hendrerit in vulputte velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo"
text = "Das Funktionsprinzip der Steganographie beruht darauf, dass ein Außenstehender die Existenz der steganographierten Information nicht erkennt. Dadurch unterscheidet Steganographie sich von der Kryptographie, bei der ein Außenstehender zwar um die Existenz von Informationen weiß, aber aufgrund der Verschlüsselung nicht in der Lage ist, den Inhalt zu verstehen. Beispiel Schickt Alice an Bob eine Nachricht, ersetzt aber vor dem Verschicken jeden Buchstaben durch den, der im Alphabet jeweils fünf Stellen weiter steht, so handelt es sich um Kryptographie (Cäsar-Chiffre). Walter, eine außenstehende Person (vielleicht ein Gefängniswärter), fängt die Nachricht beim Transport ab, kann sie aber ohne Kenntnis des Verschlüsselungsverfahrens nicht verstehen. Er sieht aber, dass eine Nachricht von Alice an Bob gesandt wurde. Wenn es in seiner Macht steht, ändert er die Nachricht oder stellt sie Bob nicht zu. Schickt Alice Bob dagegen eine Nachricht in Form eines (belanglosen) Gedichts, bei dem die Anfangsbuchstaben der Zeilen hintereinander gelesen die eigentliche Nachricht bilden, so kann der außenstehende Walter zwar sehen, dass Alice Bob eine Nachricht sendet. Der Inhalt, den Walter wahrnimmt, entspricht aber nicht der relevanten Nachricht von Alice an Bob. Die Wahrscheinlichkeit, dass Walter die Nachricht verändert oder blockiert, ist mangels Interesse gering. Dies ist Steganographie. In der Steganographie verwendet man als Szenario in der Regel den Nachrichtenversand von einem Sender zu einem Empfänger. Auch die Datenspeicherung kann darauf abgebildet werden; in dem Fall handelt es sich um Kommunikation mit sich selbst (Sender = Empfänger). Dieser Spezialfall wird aber üblicherweise vernachlässigt. Sehr ähnlich zur Steganographie sind nicht-wahrnehmbare digitale Wasserzeichen, deren Zielsetzung sich jedoch unterscheidet. Steganographie will Vertraulichkeit sichern, wohingegen digitale Wasserzeichen das Hauptaugenmerk auf Robustheit legen: Je nach Einsatzzweck wird die Robustheitseigenschaft eines Wasserzeichens so gewählt, dass es bereits durch kleine Änderungen zerstört wird (für den Nachweis von verletzter Integrität des Trägers) oder sehr starke Änderungen übersteht (für das Markieren des Trägers, bspw. mit wichtigen Informationen wie Besitzer, Urheber, Aufführungsort o. ä.). Zerstört man das Wasserzeichen im letzteren Fall, so ist der Träger dadurch so degradiert, dass er nicht mehr nutzbar ist. In Abhängigkeit vom Einsatzzweck kann die Robustheit zwischen den beschriebenen Polen variiert werden. Digitale Wasserzeichen verwenden steganographische Techniken und führen daher auch die übrigen Eigenschaften dieser Techniken wie z. B. Vertraulichkeit mit sich. Im Bedarfsfall werden diese übrigen Eigenschaften degradiert, um die Robustheit zu erhalten, genau wie bei Steganographie u. a. die Robustheit gelockert werden kann, um die Vertraulichkeit zu sichern."

number_of_bits = len(text) * 8
number_of_pixel = width * height
# pixel_offset = 1
pixel_offset = int(number_of_pixel / number_of_bits)

if pixel_offset == 0:
    print("Text to large")
    sys.exit()
print("Pixel Offset: ", str(pixel_offset))

# ascii_list = text_to_ascii(text)
binary_list = text_to_binary(text)

# Concat all binary chars to one long string
# in order to iterate over it char by char and not element by element
binary_string = "".join(binary_list)

# print(ascii_list)
# print(binary_list)
# print(binary_string)

binary_string_index = 0  # Index of current bit to insert
encoded_img = Image.new(img.mode, img.size)
for i in range(0, pixel_array.size, pixel_offset):
    pixel = pixel_array[i]  # Pixel has a value between 0 and 254
    if binary_string_index < len(binary_string):
        # convert value from pixel to binary with 10 bit and add text bit
        encoded_pixel = format(pixel, "08b")[:-1] + binary_string[binary_string_index]
        pixel_array[i] = int(encoded_pixel, 2)
        binary_string_index += 1
    else:
        break

result = pixel_array.reshape((height, width))
result = result.astype(np.uint8)

encoded_img = Image.fromarray(result)
encoded_img.save(
    "katze_encoded.png", "PNG", quality=100, optimize=False, progressive=False
)
