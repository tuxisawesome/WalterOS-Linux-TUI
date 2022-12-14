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
        print("Press 4 to list all applications")
        print("Press 5 followed by the name of a app to update the app")
        print("Press b to go back")
        print("Press e to exit")
        choice = input(f"WalterOS::{currentversion} | wpkg> ")
        if choice == "1":
            appinstall.checksysupdate()

        elif choice.startswith("2"):
            apptoinstall = choice[2:]
            appinstall.installapp(apptoinstall)
        elif choice.startswith("3"):
            apptoremove = choice[2:]
            appinstall.removeapp(apptoremove)
        elif choice == "4":
            appinstall.listapps()
        elif choice.startswith("5"):
            apptoupdate = choice[2:]
            appinstall.checkappupdate(apptoupdate)
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
        print("Press r followed by the app to run the app")
        print("Press p for power options")
        print("Press e to exit")
        choice = input(f"WalterOS::{currentversion}> ")
        if choice == "1":
            execpkgloop()
        elif choice == "e" or choice == "E":
            print("Bye")
            sys.exit()
        elif choice == "p" or choice == "P":
            print("s for shutdown, r for restart")
            choice = input(f"WalterOS::{currentversion} | power> ")
            if choice == "s" or choice == "S":
                os.system("poweroff")
                os.system("shutdown")
            elif choice == "p" or choice == "P":
                os.system("reboot")
        elif choice.startswith("r"):
            app = choice[2:]
            try:
                appinstall.runapp(app)
            except:
                print("The app is not there...")
        print("")
    
    







execloop()


