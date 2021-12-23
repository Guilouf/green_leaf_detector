import numpy
from PIL import Image

rgb_im = Image.open('data/test_tom.jpeg').convert('RGB')
hsv_im = rgb_im.convert('HSV')

rgb_nump = numpy.asarray(rgb_im)
hsv_nump = numpy.asarray(hsv_im)

# Extract Hue
H = hsv_nump[:, :, 0]

# Extract saturation
S = hsv_nump[:, :, 1]

# Extract Value (brightness)
B = hsv_nump[:, :, 2]

# Find all green pixels, i.e. where 100 < Hue < 140
lo, hi = 70, 120

# Rescale to 0-255, rather than 0-360 because we are using uint8
lo = int((lo * 255) / 360)
hi = int((hi * 255) / 360)
green = numpy.where((H > lo) & (H < hi) & (S > 10) & (B > 50))


rgb_nump[green] = [0, 255, 0]


img = Image.fromarray(rgb_nump)
img.show()
