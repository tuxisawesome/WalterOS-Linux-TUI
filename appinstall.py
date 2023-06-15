import os
import sys
import requests

def installapp(name):
    try:
        appavailable = False

        d = open(f"sources.conf", "r")
        print("Checking package sources...")
        for index, line in enumerate(d):
            if appavailable:
                weburl = line.strip()[:-2]
                break
            if line.strip() == name:
                print(f"Found {name} in sources!")
                appfoldername = line.strip()
                appavailable = True
                continue
    
        d.close()
        if appavailable == False:
            print("App not found!")
            return 1
        print(f"Are you sure you want to install {name}?")
        choice = input(f"N or n for no, or anything else for yes: ")
        if choice != "N" or choice != "n":
            os.system(f"git clone {weburl} apps/{name}")
            os.system(f"python3 apps/{name}/setup.py")
            print(f"Installed {name}")
        else:
            print("Aborted")
    except:
        print("Installing failed")

def listapps():
    counter = 0
    d = open(f"sources.conf", "r")
    print("Checking package sources...")
    print("-----------------------")
    for index, line in enumerate(d):
        if line[0] == "#":
            continue
        if line[0] == "s":
            if line[1] == "@":
                continue
        print()
        print(line)
        print()
        
    print("-----------------------")
    d.close()


def runapp(app):
    appavailable = False
    appfoldername = False
    weburl = False

    d = open(f"sources.conf", "r")
    print("Checking package sources...")

    for index, line in enumerate(d):
        if appavailable:
            weburl = line.strip()
            break
        if line.strip() == app:
            print(f"Found {app} in sources!")
            appfoldername = line.strip()
            appavailable = True
            continue

    d.close()
    if weburl == False or appfoldername == False or appavailable == False:
        return 1
    os.system(f"python3 apps/{app}/app.py")
    return 0
def removeapp(name):
    try:
        appavailable = False
        appfoldername = False
        weburl = False
        d = open(f"sources.conf", "r")
        print("Checking package sources...")
        for index, line in enumerate(d):
            if appavailable:
                weburl = line.strip()
                break
            if line.strip() == name:
                print(f"Found {name} in sources!")
                appfoldername = line.strip()
                appavailable = True
                continue
        
        d.close()
        if weburl == False or appfoldername == False or appavailable == False:
            print("App not there!")
            return 1
        print(f"Are you sure you want to remove {name}?")
        choice = input(f"N or n for no, or anything else for yes: ")
        if choice != "N" or choice != "n":
            os.system(f"rm -rf apps/{name}")
            print(f"Removed {name}")
        else:
            print("Aborted.")
    except:
        print("Removing failed.")

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

    appavailable = False
    appfoldername = False
    weburl = False
    d = open(f"sources.conf", "r")
    print("Checking package sources...")
    for index, line in enumerate(d):
        if appavailable2:
            weburl = line.strip()[:-2]
            break
        if appavailable:
            appavailable2 = True
            continue
        if line.strip() == app:
            print(f"Found {app} in sources!")
            appfoldername = line.strip()
            appavailable = True
            continue

    d.close()
    if weburl == False or appfoldername == False or appavailable == False:
        print("App not found!")
        return 1
    cv = open(f"apps/{app}/version.txt")

    currentversion = cv.readline()
    cv.close()

    latestversion = requests.get(weburl).text
    if latestversion == currentversion:
        print("You are on the latest version!")
    else:
        print(f"Current version of {app} is {currentversion}")
        print(f"Latest version of {app} is {latestversion}")
        print(f"Are you sure you want to update {app}?")
        choice = input("y for yes, or anything else for no: ")
        if choice == "y" or choice == "Y":
            print(f"Updating {app} to {latestversion}")
            os.system(f"cd apps/{app} && git pull")
            print("Updated!")