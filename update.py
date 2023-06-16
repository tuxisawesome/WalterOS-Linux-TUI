import requests, os


def checksysupdate():
    latestversion = requests.get("https://raw.githubusercontent.com/tuxisawesome/WalterOS-Linux-TUI/master/version.txt", headers={'User-Agent': 'Custom'}).text
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
    appavailable2 = False
    appfoldername = False
    weburl = False
    d = open(f"sources.conf", "r")
    print("Checking package sources...")
    for index, line in enumerate(d):
        if appavailable2:
            weburl = line.strip()
            weburl = weburl[2:]
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

    latestversion = requests.get(weburl, headers={'User-Agent': 'Custom'}).text
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