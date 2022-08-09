import os
print("WalterOS-Linux-TUI [BOT]")
with open("version.txt", "r") as r:
    currentversion = r.readline()
    print(f"* {currentversion} is the current version")
    r.close()
with open("version.txt", "w") as w:
    latestversion = str(float(currentversion) + 0.01)
    print(f"* changed version to {latestversion}")
    w.write(latestversion)
    w.close()
print(":-> Update pushed")