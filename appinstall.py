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
                weburl = line.strip()
                weburl = weburl[2:]
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
        choice = input(f"Y or y for yes, or anything else for no: ")
        if choice == "Y" or choice == "y":
            if os.path.isdir(f"apps/{name}"):
                print("")
                print(f"{name} is already installed!")
                print("")
            else:
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
    s1 = False
    s2 = False
    x = ""
    for index, line in enumerate(d):
        if line[0] == "#":
            continue
        elif line == "":
            continue
        elif line[0] == "s":
            if line[1] == "@":
                if s2 == True:
                    x = line[2:]
                    s1 = False
                    s2 = False
                    continue
                if s1 == True:
                    s2 = True
                    continue
        print(line.rstrip("\n"))
        s1 = True
        
    print("-----------------------")
    d.close()


def runapp(app):
    appavailable = False
    appfoldername = False
    weburl = False

    d = open(f"sources.conf", "r")
    #print("Checking package sources...")

    for index, line in enumerate(d):
        if appavailable:
            weburl = line.strip()
            break
        if line.strip() == app:
            #print(f"Found {app} in sources!")
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
        choice = input(f"Y or y for yes, or anything else for no: ")
        if choice == "Y" or choice == "y":
            os.system(f"rm -rf apps/{name}")
            print(f"Removed {name}")
        else:
            print("Aborted.")
    except:
        print("Removing failed.")
