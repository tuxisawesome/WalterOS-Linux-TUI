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
        print(f"Are you sure you want to update {currentversion} to {latestversion}?")
        choice = input("y for yes, or anything else for no: ")
        if choice == "y" or choice == "Y":
            print(f"Updating {currentversion} to {latestversion}")
            os.system("git pull")
            print("Updated. Please restart computer...")
    else:
        print("You are on the latest version!")


def checkappupdate(app):
    d = open(f"{app}/config.txt", "r")
    uname = d.readline()
    repo = d.readline()
    currentversion = d.readline()
    d.close()

    latestversion = requests.get(f"https://raw.githubusercontent.com/{uname}/{repo}/master/version.txt").text
    if latestversion == currentversion:
        print("You are on the latest version!")
    else:
        print(f"Current version of {app} is {currentversion}")
        print(f"Latest version of {app} is {latestversion}")
        print(f"Are you sure you want to update {app}?")
        choice = input("y for yes, or anything else for no: ")
        if choice == "y" or choice == "Y":
            print(f"Updating {app} to {latestversion}")
            os.system(f"cd {app} && git pull")
            print("Updated!")