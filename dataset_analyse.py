import os
import csv
from detect_green import GreenDetect

directory = 'data'

with open('analysed/results.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['DOSSIER', 'NOMBRE PIXELS VERTS'])

    for root, dirs, files in os.walk(directory):
        for filename in files:
            complete_name = os.path.join(root, filename)
            analysed = GreenDetect(complete_name)

            # save "green" image to another folder, with existing sub-folders
            analysed.save_green_image(os.path.join('analysed', root), f'{filename}')

            writer.writerow([complete_name, analysed.green_pixels_number])
