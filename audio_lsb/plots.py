from scipy.io import wavfile
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
        result.append(format(element, "016b"))
    return result


text = (
    16
    * "Das Funktionsprinzip der Steganographie beruht darauf, dass ein Außenstehender die Existenz der steganographierten Information nicht erkennt. Dadurch unterscheidet Steganographie sich von der Kryptographie, bei der ein Außenstehender zwar um die Existenz von Informationen weiß, aber aufgrund der Verschlüsselung nicht in der Lage ist, den Inhalt zu verstehen. Beispiel Schickt Alice an Bob eine Nachricht, ersetzt aber vor dem Verschicken jeden Buchstaben durch den, der im Alphabet jeweils fünf Stellen weiter steht, so handelt es sich um Kryptographie (Cäsar-Chiffre). Walter, eine außenstehende Person (vielleicht ein Gefängniswärter), fängt die Nachricht beim Transport ab, kann sie aber ohne Kenntnis des Verschlüsselungsverfahrens nicht verstehen. Er sieht aber, dass eine Nachricht von Alice an Bob gesandt wurde. Wenn es in seiner Macht steht, ändert er die Nachricht oder stellt sie Bob nicht zu. Schickt Alice Bob dagegen eine Nachricht in Form eines (belanglosen) Gedichts, bei dem die Anfangsbuchstaben der Zeilen hintereinander gelesen die eigentliche Nachricht bilden, so kann der außenstehende Walter zwar sehen, dass Alice Bob eine Nachricht sendet. Der Inhalt, den Walter wahrnimmt, entspricht aber nicht der relevanten Nachricht von Alice an Bob. Die Wahrscheinlichkeit, dass Walter die Nachricht verändert oder blockiert, ist mangels Interesse gering. Dies ist Steganographie. In der Steganographie verwendet man als Szenario in der Regel den Nachrichtenversand von einem Sender zu einem Empfänger. Auch die Datenspeicherung kann darauf abgebildet werden; in dem Fall handelt es sich um Kommunikation mit sich selbst (Sender = Empfänger). Dieser Spezialfall wird aber üblicherweise vernachlässigt. Sehr ähnlich zur Steganographie sind nicht-wahrnehmbare digitale Wasserzeichen, deren Zielsetzung sich jedoch unterscheidet. Steganographie will Vertraulichkeit sichern, wohingegen digitale Wasserzeichen das Hauptaugenmerk auf Robustheit legen: Je nach Einsatzzweck wird die Robustheitseigenschaft eines Wasserzeichens so gewählt, dass es bereits durch kleine Änderungen zerstört wird (für den Nachweis von verletzter Integrität des Trägers) oder sehr starke Änderungen übersteht (für das Markieren des Trägers, bspw. mit wichtigen Informationen wie Besitzer, Urheber, Aufführungsort o. ä.). Zerstört man das Wasserzeichen im letzteren Fall, so ist der Träger dadurch so degradiert, dass er nicht mehr nutzbar ist. In Abhängigkeit vom Einsatzzweck kann die Robustheit zwischen den beschriebenen Polen variiert werden. Digitale Wasserzeichen verwenden steganographische Techniken und führen daher auch die übrigen Eigenschaften dieser Techniken wie z. B. Vertraulichkeit mit sich. Im Bedarfsfall werden diese übrigen Eigenschaften degradiert, um die Robustheit zu erhalten, genau wie bei Steganographie u. a. die Robustheit gelockert werden kann, um die Vertraulichkeit zu sichern."
)
binary_list = text_to_binary(text)
binary_string = "".join(binary_list)

fs, data = wavfile.read("sound.wav")
samples = np.array(data)

dnumber_of_bits = len(text) * 8
number_of_frames = np.array(data).shape[0]
bits_per_frame = 8

print("Number of text bits:\t", len(binary_string))
print("Number of frames:\t", number_of_frames)
print("Required frames:\t", len(binary_string) / bits_per_frame)

binary_string_index = 0  # Index of current bit to insert
new_wav = np.zeros(number_of_frames)
for i in range(0, number_of_frames):
    sample = samples[i]  # Pixel has a value between 0 and 254
    if binary_string_index < len(binary_string):

        text_bits = binary_string[
            binary_string_index : binary_string_index + bits_per_frame
        ]

        # convert value from pixel to binary with 10 bit and add text bit
        encoded_frame = format(sample, "016b")[:-bits_per_frame] + text_bits
        new_wav[i] = int(encoded_frame, 2)
        binary_string_index += bits_per_frame
    else:
        new_wav[i] = sample

wavfile.write("encoded.wav", fs, np.asarray(new_wav, dtype=np.int16))
