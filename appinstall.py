import os
import sys


def installapp(url, name):
    try:
        print(f"Are you sure you want to install {name}?")
        choice = input(f"N or n for no, or anything else for yes: ")
        if choice is not "N" or choice is not "n":
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
    if choice is not "N" or choice is not "n":
        os.system(f"rm -rf {name}")
        print(f"Removed {name}")
    else:
        print("Aborted.")


# Update time

def checksysupdate():
    pass

