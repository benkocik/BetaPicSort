# Programmer: Ben Kocik
# Description: Automatically sorts pictures into dated folders

# Imports
import os
import time

def main():
    # Mount the google drive folder
    os.system("sudo rclone mount --allow-other --daemon picsort: " + histPath)
    histPath = os.path.join("/mnt", "HistDrive")

    # Sort through pictures
    dumpPath = os.path.join(histPath, "ToSort")
    for pic in os.listdir(dumpPath):
        picDate = time.ctime(os.path.getmtime(pic))
        print(picDate)
        #for f in os.walk(histPath):


    # Unmount the google drive folder
    os.system("fusermount -u " + histPath)



if __name__ == "__main__":
    main()