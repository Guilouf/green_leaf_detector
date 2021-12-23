import numpy
from PIL import Image


class GreenDetect:

    # Hue threshold values (rescaled from 360° to uint8)
    lo = int((70 * 255) / 360)
    hi = int((150 * 255) / 360)

    # Saturation threshold
    sat_thres = 30

    # Brightness threshold
    bright_thres = 20

    def __init__(self, filename):
        rgb_im = Image.open(filename).convert('RGB')
        hsv_im = rgb_im.convert('HSV')

        self.rgb_nump = numpy.asarray(rgb_im)
        hsv_nump = numpy.asarray(hsv_im)

        # Extract Hue
        h = hsv_nump[:, :, 0]

        # Extract saturation
        s = hsv_nump[:, :, 1]

        # Extract Value (brightness)
        b = hsv_nump[:, :, 2]

        self.conditions = (h > self.lo) & (h < self.hi) & (s > self.sat_thres) & (b > self.bright_thres)

    @property
    def pixel_ratio(self):
        """Ratio between green pixels and the total amount of pixels from the input image"""
        return self.green_pixels_number / self.total_pixels_number

    @property
    def green_pixels_number(self):
        return numpy.count_nonzero(self.conditions)

    @property
    def total_pixels_number(self):
        return self.rgb_nump.shape[0] * self.rgb_nump.shape[1]

    def show_binary_image(self):
        Image.fromarray(self.conditions).show()

    def show_green_image(self):
        """rgb image in which all affiliated green pixels are turned into pure green"""
        green = numpy.where(self.conditions)
        self.rgb_nump[green] = [0, 255, 0]
        img = Image.fromarray(self.rgb_nump)
        img.show()


if __name__ == "__main__":
    GreenDetect('data/test_tom.jpeg')
