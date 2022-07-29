import appinstall
import os
import sys
import time
cv = open("version.txt", "r")
currentversion = cv.readline()
cv.close()

print(f"WalterOS version {currentversion}")
def execpkgloop():
    keepexecpkgloop = True
    while keepexecpkgloop:
        print("Press 1 for Checking system update")
        print("Press 2 followed by the app for installing a app")
        print("Press 3 followed by the app to remove the app")
        print("Press b to go back")
        print("Press e to exit")
        choice = input(f"WalterOS::{currentversion} | wpkg> ")
        if choice == "1":
            appinstall.checksysupdate()

        elif choice.startswith("2"):
            apptoinstall = choice[2:]
            appurl = input("The URL of the app: ")
            appinstall.installapp(appurl, apptoinstall)
        elif choice.startswith("3"):
            apptoremove = choice[2:]
            appinstall.removeapp(apptoremove)
        elif choice == "e" or choice == "E":
            print("Bye")
            sys.exit()
        elif choice == "b" or choice == "B":
            keepexecpkgloop = False
        else:
            pass
        print("")

def execloop():
    keepexecloop = True
    while keepexecloop:
        print("Press 1 for Package Manager")
        print("Press e to exit")
        choice = input(f"WalterOS::{currentversion}> ")
        if choice == "1":
            execpkgloop()
        elif choice == "e" or choice == "E":
            print("Bye")
            sys.exit()
        print("")
    
    







execloop()


