import os
import sys
import mimetypes

# get the path of the directory in which the files must be renamed
args = sys.argv[1]

# change the directory to the passed directory
os.chdir(args)

# listing the contents of the current directory to get all the files in it as a array
files = os.listdir()


# # loop through the directory files and rename them
for i, image in enumerate(files):
    if mimetypes.guess_type(image)[0] == "image/jpeg":
        os.rename(image, "image-" + str(i) + ".jpg")
    elif mimetypes.guess_type(image)[0] == "image/png":
        os.rename(image, "image-" + str(i) + ".png")
    else:
        continue
