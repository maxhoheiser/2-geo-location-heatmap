import exifread

"""
Script to generate a heatmap from geo locations derived from different sources
1. google location history
2. gpx files from fitness tracker
3. location from pictures
"""

#=============================================================================
ROOT = "/"
IMAGES = ["jpeg", "jpg", "png", "raw"]
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


#=============================================================================



#=============================================================================
# main code loop
files = file_crawler(ROOT, IMAGES)



#=============================================================================


