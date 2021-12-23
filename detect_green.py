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

conditions = (H > lo) & (H < hi) & (S > 10) & (B > 50)
green = numpy.where(conditions)


green_pixel_number = numpy.count_nonzero(conditions)
total_pixel_number = rgb_nump.shape[0] * rgb_nump.shape[1]
print(green_pixel_number, total_pixel_number, green_pixel_number / total_pixel_number)

# Binary image
Image.fromarray(conditions).show()

# Green colored image
rgb_nump[green] = [0, 255, 0]
img = Image.fromarray(rgb_nump)
img.show()
