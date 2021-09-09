# Programmer: Ben Kocik
# Description: Automatically sorts pictures into dated folders

# Imports
import os
import subprocess
import time

def main():
    # Mount the google drive folder
    histPath = os.path.join("/mnt", "HistDrive")
    os.system("sudo rclone mount --allow-other --daemon picsort: " + histPath)
    time.sleep(5)   # Wait 5 seconds for drive to connect

    # Sort through pictures
    dumpPath = os.path.join(histPath, "ToSort")
    for pic in os.listdir(dumpPath):
        picDate = time.ctime(os.path.getmtime(os.path.join(dumpPath, pic)))
        picMonth = picDate.split()[1]   # May be used later to sort by Fall/Spring term
        picYear = picDate.split()[4]    # String of year of picture
        print(picYear)
        for f in os.listdir(histPath):
            # Confirm it is a directory
            if os.path.isdir(f):
                # Check decade folder
                if f[:2] == picYear[:2]:
                    print(f)
                    print(f[:2])
                    for j in os.listdir(os.path.join(histPath, f)):
                        print(j)
                        # Confirm it is a directory
                        if os.path.isdir(j):
                            # Check specific year folder
                            if j == picYear:
                                subprocess.call("mv " + pic + " " + os.path.join(os.path.join(histPath, f), j))   # Move file into folder

    # Unmount the google drive folder
    os.system("sudo fusermount -u " + histPath)

if __name__ == "__main__":
    main()