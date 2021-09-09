# Programmer: Ben Kocik
# Description: Automatically sorts pictures into dated folders

# Imports
import os
import time

def main():
    # Mount the google drive folder
    histPath = os.path.join("/mnt", "HistDrive")
    os.system("sudo rclone mount --allow-other --daemon picsort: " + histPath)
    time.sleep(5)

    # Sort through pictures
    dumpPath = os.path.join(histPath, "ToSort")
    for pic in os.listdir(dumpPath):
        picDate = time.ctime(os.path.getmtime(os.path.join(dumpPath, pic)))
        picMonth = picDate.split()[1]   # May be used later to sort by Fall/Spring term
        picYear = picDate.split()[4]    # String of year of picture
        for f in os.walk(histPath):
            # Check decade folder
            if f[:3] == picYear[:3]:
                for j in os.walk(os.path.join(histPath, f)):
                    # Check specific year folder
                    if j == picYear:
                        os.system("mv " + pic + " " + os.path.join(os.path.join(histPath, f), j))   # Move file into folder

    # Unmount the google drive folder
    os.system("sudo fusermount -u " + histPath)

if __name__ == "__main__":
    main()