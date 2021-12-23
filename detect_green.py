import numpy
from PIL import Image


class GreenDetect:

    # Hue threshold values (rescaled from 360° to uint8)
    lo = int((70 * 255) / 360)
    hi = int((120 * 255) / 360)

    # Saturation threshold
    sat_thres = 10

    # Brightness threshold
    bright_thres = 50

    def __init__(self, filename):
        rgb_im = Image.open(filename).convert('RGB')
        hsv_im = rgb_im.convert('HSV')

        rgb_nump = numpy.asarray(rgb_im)
        hsv_nump = numpy.asarray(hsv_im)

        # Extract Hue
        h = hsv_nump[:, :, 0]

        # Extract saturation
        s = hsv_nump[:, :, 1]

        # Extract Value (brightness)
        b = hsv_nump[:, :, 2]

        conditions = (h > self.lo) & (h < self.hi) & (s > self.sat_thres) & (b > self.bright_thres)
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


if __name__ == "__main__":
    GreenDetect('data/test_tom.jpeg')
