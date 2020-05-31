import os
import glob
import subprocess

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
#functions
def filebrowser(folder, ext=""):
    "Returns files with an extension"
    os.chdir(folder)
    return [f for f in glob.glob(f"*{ext}")]

def file_crawler(folder, extention):
    "Returns a list with all files in root and each sub directory"
    files = [os.path.join(root, name)
        for root, dirs, files in os.walk(folder)
        for name in files
        if name.endswith((extention))]
    return files

def all_files(folder, ext_list):
    "Returns a dictionary with extentions as key and list of files as value"
    file_dict = dict()
    for ext in ext_list:
        file_dict[ext] = list(file_crawler(folder, ext))
    return file_dict

def find_unique(files_dict):
    "Find unique files by names"
    files_dict_unique = dict()
    name_list = []
    # first scann for already converted files
    if files_dict["gpx"] != None:
        value_list = []
        for value in files_dict["gpx"]:
            name = (value.split('/')[-1]).split('.')[0]
            if name not in name_list:
                name_list.append(name)
                value_list.append(value)
        files_dict_unique["gpx"] = value_list
    # scann for dublicates of all other file types        
    for key, values in files_dict.items():
        if key == "gpx":
            continue
        value_list = []
        for value in values:
            name = (value.split('/')[-1]).split('.')[0]
            if name not in name_list:
                name_list.append(name)
                value_list.append(value)
        files_dict_unique[key] = value_list
    return files_dict_unique

def convert(file, extention, output_dir):
    "Runs gpsbabel on all input files - converts them to gpx format"
    #output_file = ("\"" + output_dir + "/" + (file.split('/')[-1]).split('.')[0] + ".gpx" + "\"")
    #file = ("\"" + file + "\"")
    output_file = (output_dir + "/" + (file.split('/')[-1]).split('.')[0] + ".gpx")
    bashCommands = {
        # gpsbabel -t -i [input format] -f [input file name] -o gpx -F [output file name]
        # garmin_fit
        "fit":["gpsbabel", "-t ", "-i", "garmin_fit", "-f", file,
               "-o", "gpx", "-F", output_file],
        # gtrnctr
        "tcx":["gpsbabel", "-t", "-i", "gtrnctr", "-f", file,
               "-o", "gpx", "-F", output_file],
        }
    command = subprocess.run(bashCommands[extention])

def intersperse(lst, item):
    result = [item] * (len(lst) * 2)
    result[1::2] = lst
    return result

def combine(input_files, output):
    "Runs ... and combines all given input_files to one gpx file"
    # gpsbabel -i gpx -f filename -f filename2 -f filename3 -o gpx -F "All.gpx"
    files = intersperse(input_files,"-f")
    bashCommand = ["gpsbabel", "-i", "gpx"] + files + ["-o", "gpx", "-F", output]
    command = subprocess.run(bashCommand)
#=============================================================================






#=============================================================================
# convert files 
#=============================================================================
# scann and build list with all files depending on extention in given folder
files_dict = all_files(FOLDER_GPX_INPUT, EXTENTIONS )


# find unique files 
files_dict = find_unique(files_dict)


# converte all found unique files to gpx
ext_conv = EXTENTIONS
ext_conv.remove("gpx")
new_gpx = []
for ext in ext_conv:
    if files_dict[ext] != None:
        for file in files_dict[ext]:
            convert(file, ext, FOLDER_GPX_OUTPUT)
            new_gpx.append(file)

files_dict["gpx"].extend(new_gpx)
       

# merge all gpx files to single gpx file & delete gpx files
output = FOLDER_GPX_OUTPUT + "/merge.gpx"
combine(files_dict["gpx"], output)


#=============================================================================
# create heatmap
        