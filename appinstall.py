import os
import sys
import requests

def installapp(url, name):
    try:
        print(f"Are you sure you want to install {name}?")
        choice = input(f"N or n for no, or anything else for yes: ")
        if choice != "N" or choice != "n":
            os.system(f"git clone {url} {name}")
            os.system(f"python3 {name}/setup.py")
            print(f"Installed {name}")
        else:
            print("Aborted")
    except:
        print("Installing failed")

def runapp(name):
    os.system(f"python3 {name}/app.py")

def removeapp(name):
    print(f"Are you sure you want to remove {name}?")
    choice = input(f"N or n for no, or anything else for yes: ")
    if choice != "N" or choice != "n":
        os.system(f"rm -rf {name}")
        print(f"Removed {name}")
    else:
        print("Aborted.")


# Update time

def checksysupdate():
    latestversion = requests.get("https://raw.githubusercontent.com/tuxisawesome/WalterOS-Linux-TUI/master/version.txt").text
    cv = open("version.txt", "r")
    currentversion = cv.readline()
    cv.close()
    print(f"Version {currentversion} is on system")
    print(f"Version {latestversion} is the latest version")
    print("")
    if latestversion != currentversion:
        pass
    else:
        print("You are on the latest version!")


