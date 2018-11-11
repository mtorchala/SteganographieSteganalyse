import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_original = Image.open("katze_gs.png")
img_encoded = Image.open("katze_encoded.png")

np_original = np.array(img_original)
np_encoded = np.array(img_encoded)

plt.imshow(np_encoded - np_original)
plt.show()

# 640x427 = 273.280 mögliche Bits
# 34.160 Mögliche Buchstaben (inkl. Leerzeichen u.ä.)
