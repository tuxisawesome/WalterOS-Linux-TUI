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



def installapp(name,silent=False,nofirstrun=False, ff=False):
    try:
        appavailable = False
        if ff:
            d = open(f"etc/sources.conf", "r")
        else:
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
            if ff:
                prefix = "bin/"
            else:
                prefix = "apps/"
            if os.path.isdir(f"{prefix}{name}"):
                if not silent:
                    print("")
                    print(f"{name} is already installed!")
                    print("")
                return 3
            else:
                os.system(f"git clone {weburl} {prefix}{name} >/dev/null 2>&1")
                if not nofirstrun:
                    os.system(f"cd {prefix}{name} && python3 setup.py")
                if not silent:
                    print(f"Installed {name}")
                return 0
        else:
            print("Aborted")
    except:
        print(f"Installing failed for app {name}")

def listapps(ff=False):
    counter = 0
    if ff:
        d = open(f"etc/sources.conf", "r")
        apps = []
        for line in enumerate(d):
            if line[0] == "#":
                continue
            elif line == "":
                continue
            elif line[0] == "s":
                continue
            if os.path.isdir(f"bin/{line.rstrip("\n")}"):
                apps.append(line.rstrip("\n"))
        return apps

    else:
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


def runapp(app, ff=False):
    appavailable = False
    appfoldername = False
    weburl = False
    if ff:
        d = open(f"etc/sources.conf", "r")
    else:
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
    if ff:
        os.system(f"cd bin/{app} && python3 app.py")
    else:
        os.system(f"cd apps/{app} && python3 app.py")
    return 0
def removeapp(name, silent=False, ff=False):
    try:
        appavailable = False
        appfoldername = False
        weburl = False
        if ff:
            d = open(f"etc/sources.conf", "r")
        else:
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
            if ff:
                os.system(f"rm -rf bin /{name}")
            else:
                os.system(f"rm -rf apps/{name}")
            if not silent:
                print(f"Removed {name}")
        else:
            print("Aborted.")
    except:
        print("Removing failed.")
