import exifread
import os

"""
Script to generate a heatmap from geo locations derived from different sources
1. google location history
2. gpx files from fitness tracker
3. location from pictures
"""

#=============================================================================
ROOT = "/"
IMAGES = ("jpeg", "jpg", "raw")
#=============================================================================


#=============================================================================
#functions

def file_crawler(folder, extention):
    "Returns a list with all files in root and each sub directory"
    files = [os.path.join(root, name)
        for root, dirs, files in os.walk(folder)
        for name in files
        if name.endswith((extention))]
    return files

def gps_extractor(file):
    gps_keys = ['GPS GPSAltitude', 'GPS GPSLatitude', 'EXIF DateTimeOriginal', 'GPS GPSLongitude']
    gps = dict()
    with open(path_name, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    for key in tags.keys():
        if key in gps_keys:
            gps[key] = tags[key].printable
    #gps[key] = [tags[key] for key in tags.keys() if 'GPS' in key]
    if len(gps) == 0:
        return None
    else: 
        return gps

#=============================================================================




#=============================================================================
# main code loop
folder = r"/home/max/ExpanDrive/Google Drive/3.1 Code Repository/2-geo-location-heatmap/test_fotos"
files = file_crawler(folder, IMAGES)
files_dict = dict()
for file in files:
    files_dict[file] = gps_extractor(file)




#=============================================================================


