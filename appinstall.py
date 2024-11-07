import os
import sys
import requests


def checkforApp(name,silent=False):
    appavailable = False

    d = open(f"sources.conf", "r")
    if not silent:
        print("Checking package sources...")
    for index, line in enumerate(d):
        if appavailable:
            weburl = line.strip()
            weburl = weburl[2:]
            break
        if line.strip() == name:
            if not silent:
                print(f"Found {name} in sources!")
            appfoldername = line.strip()
            appavailable = True
            continue
    d.close()

    if appavailable:
        return 0
    else:
        return 1



def installapp(name,silent=False,nofirstrun=False):
    try:
        appavailable = False

        d = open(f"sources.conf", "r")
        if not silent:
            print("Checking package sources...")
        for index, line in enumerate(d):
            if appavailable:
                weburl = line.strip()
                weburl = weburl[2:]
                break
            if line.strip() == name:
                if not silent:
                    print(f"Found {name} in sources!")
                appfoldername = line.strip()
                appavailable = True
                continue
    
        d.close()
        choice = ""
        if appavailable == False:
            print("App not found!")
            return 1
        if not silent:
            print(f"Are you sure you want to install {name}?")
            choice = input(f"Y or y for yes, or anything else for no: ")
        else:
            choice = "Y"
        if choice == "Y" or choice == "y":
            if os.path.isdir(f"apps/{name}"):
                if not silent:
                    print("")
                    print(f"{name} is already installed!")
                    print("")
                return 3
            else:
                os.system(f"git clone {weburl} apps/{name} >/dev/null 2>&1")
                if not nofirstrun:
                    os.system(f"cd apps/{name} && python3 setup.py")
                if not silent:
                    print(f"Installed {name}")
                return 0
        else:
            print("Aborted")
    except:
        print(f"Installing failed for app {name}")

def listapps():
    counter = 0
    d = open(f"sources.conf", "r")
    print("-----------------------------------")
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
        # x = installapp(name=line.rstrip("\n"),silent=True,nofirstrun=True)
        if os.path.isdir(f"apps/{line.rstrip("\n")}"):
            print("*   ",end="")
        elif checkforApp(line.rstrip("\n"),True) == 1:
            print("!   ",end="")
        else:
            print("    ",end="")
        print(line.rstrip("\n"))
        s1 = True
        
    print("-----------------------------------")
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
    os.system(f"cd apps/{app} && python3 app.py")
    return 0
def removeapp(name, silent=False):
    try:
        appavailable = False
        appfoldername = False
        weburl = False
        d = open(f"sources.conf", "r")
        if not silent:
            print("Checking package sources...")
        for index, line in enumerate(d):
            if appavailable:
                weburl = line.strip()
                break
            if line.strip() == name:
                if not silent:
                    print(f"Found {name} in sources!")
                appfoldername = line.strip()
                appavailable = True
                continue
        
        d.close()
        if weburl == False or appfoldername == False or appavailable == False:
            print("App not there!")
            return 1
        choice = ""
        if not silent:
            print(f"Are you sure you want to remove {name}?")
            choice = input(f"Y or y for yes, or anything else for no: ")
        else:
            choice = "Y"
        if choice == "Y" or choice == "y":
            os.system(f"rm -rf apps/{name}")
            if not silent:
                print(f"Removed {name}")
        else:
            print("Aborted.")
    except:
        print("Removing failed.")
