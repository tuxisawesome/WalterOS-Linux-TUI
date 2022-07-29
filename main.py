import appinstall
import os
import sys
import time

currentversion = open("version.txt", "r")
print(f"WalterOS version {currentversion}")
def execpkgloop():
    keepexecpkgloop = True
    while keepexecpkgloop:
        print("Press 1 for Package Manager")
        print("Press b to go back")
        print("Press e to exit")
        choice = input(f"WalterOS::{currentversion} | wpkg> ")
        if choice == "1":
            execpkgloop()
        elif choice == "e" or choice == "E":
            print("Bye")
            sys.exit()
        elif choice == "b" or choice == "B":
            keepexecpkgloop = False
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


