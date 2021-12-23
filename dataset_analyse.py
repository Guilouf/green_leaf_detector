import os
import csv
from detect_green import GreenDetect

directory = 'data'

with open('results.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['DOSSIER', 'RATIO surface VERT/AUTRE'])

    for root, dirs, files in os.walk(directory):
        for filename in files:
            complete_name = os.path.join(root, filename)
            analysed = GreenDetect(complete_name)
            writer.writerow([complete_name, analysed.pixel_ratio])