import os
import glob
import subprocess
import gpxpy
from gpxobject import GPXMapper


"""
Script to generate a heatmap from geo locations derived from different sources
1. google location history
2. gpx files from fitness tracker
3. location from pictures

Dependencies:
    geo-heatmap.py
    utils.py
"""

#=============================================================================
FOLDER_GPX_INPUT=r"/home/max/ExpanDrive/Google Drive/2 Second Brain/Bikepacking Routes"
FOLDER_GPX_OUTPUT=r"/home/max/ExpanDrive/Google Drive/2 Second Brain/Bikepacking Routes/gpx"
EXTENTIONS = ["tcx", "fit", "gpx"]
#=============================================================================



#=============================================================================
# convert files 

# scann and build list with all files depending on extention in given folder
file_object = GPXMapper( FOLDER_GPX_INPUT, EXTENTIONS, 100)
all_files = file_object.AllFiles()

# find unique files 
unique = file_object.FindUnique()

# converte all found unique files to gpx
file_object.ConvertAllNonGpx2Gpx( (FOLDER_GPX_INPUT + "\gpx") )
       

# merge all gpx files to single gpx file & delete gpx files
output = FOLDER_GPX_OUTPUT + "/merge.gpx"
file_object.Combine(output)


#=============================================================================
# prepare gpx for heatmap
# extract gps points
file_object.GpxExtractCoords()        