def addsource(name,version,url,ff=False):
    print()
    print(" ######### ARE YOU SURE??? ######### ")
    print(" Are you sure you want to add a new  ")
    print(" source? type Y or y for yes or any  ")

    if not ff:
        choice = input(" thing else to cancel: ")
    else:
        choice = "y"
    if choice == "Y" or "y":
        if not ff:
            with open("sources.conf","a") as w:
                w.writelines(f"\n# {name}\n{name}\ns@{url}\ns@{version}")
        else:
            with open("etc/sources.conf","a") as w:
                w.writelines(f"\n# {name}\n{name}\ns@{url}\ns@{version}")
    else:
        print("Aborted.")

def removesource(name,ff=False):
    print()
    print(" ######### ARE YOU SURE??? ######### ")
    print(" Are you sure you want to remove a   ")
    print(" source? type Y or y for yes or any  ")
    if not ff:
        choice = input(" thing else to cancel: ")
    else:
        choice = "y"
    if choice == "Y" or "y":
        if ff:
            d = open(f"etc/sources.conf", "r")
        else:
            d = open(f"sources.conf","r")
        indexname = 0
        indexver = 0
        indexurl = 0
        appavailable = False
        appavailable2 = False
        for index, line in enumerate(d):
            if appavailable2:
                indexver = index
                break
            if appavailable:
                indexurl = index
                appavailable2 = True
                continue
            if line.strip() == name:
                print(f"Found {name} in sources!")
                indexname = index
                appfoldername = line.strip()
                appavailable = True
                continue
        if not appavailable:
            pass
        else:
            with open(f"sources.conf", "r+") as f:
                lines = f.readlines()
                del lines[indexver]  # use linenum - 1 if linenum starts from 1
                f.seek(0)
                f.truncate()
                f.writelines(lines)
            with open(f"sources.conf", "r+") as f:
                lines = f.readlines()
                del lines[indexurl]  # use linenum - 1 if linenum starts from 1
                f.seek(0)
                f.truncate()
                f.writelines(lines)
            with open(f"sources.conf", "r+") as f:
                lines = f.readlines()
                del lines[indexname]  # use linenum - 1 if linenum starts from 1
                f.seek(0)
                f.truncate()
                f.writelines(lines)
            print("done")
    else:
        print("Aborted.")