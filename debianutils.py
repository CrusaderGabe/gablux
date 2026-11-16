import subprocess, re, sys, os, datetime, random, string, mintutils, mainutils

def update():
    print("Initializing Updates..")
    sources_content = """deb https://deb.debian.org/debian bookworm main /n deb https://deb.debian.org/debian bookworm-updates main /n deb https://security.debian.org/debian-security bookworm-security main"""
    subprocess.run(["sudo", "tee", "/etc/apt/sources.list"], input = sources_content, text = True, stdout = subprocess.DEVNULL, check = True)
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell = True)

def auto_update():
    print("Establishing Auto Updates..")
    new_setting = "APT::Periodic::Update-Package-Lists \"1\";"
    subprocess.run("sudo tee -a /etc/apt/apt.conf.d/20auto-upgrades", shell = True, input=new_setting,text=True,stdout=subprocess.DEVNULL)

def remove_users():
    print("Ok.. lets remove users that we do NOT need.")
    subprocess.run("awk -F: '$3 >= 1000 {print $1}' /etc/passwd", shell = True)
    print("Compare the README and Users shown.")
    print("Find the Targeted Users and Enter:")
    removeusers = mainutils.multi_line().splitlines()
    for user in removeusers:
        if not user:
            continue

        response = input(f"Remove {user} from database? [y/n]")
        if response.lower() != "y":
            print("Skipping User")
            continue

        print(f"Removing {user} from the database..")
        termination = subprocess.run(f"sudo deluser --remove-home {user}", shell = True)

        if termination.returncode == 0:
            print(f"{user} removed from the database..")
        else:
            print(f"Failed to remove {user}")

def remove_admins():
    print("Let's remove admins that aren't uh.. really admins ey?")
    subprocess.run("getent group sudo", shell = True)
    print("See any you want to remove?")
    users = mainutils.multi_line().splitlines()
    for user in users:
        if not user:
            continue

        response = input(f"Remove {user} from administration? [y/n]")
        if response.lower() != "y":
            print(f"Skipped {user}")
            continue

        print(f"Removing {user} from administration..")
        termination = subprocess.run(f"sudo gpasswd -d {user} sudo", shell = True)

        if termination.returncode == 0:
            print(f"{user} removed from administration..")
        else:
            print(f"Failed to remove {user}")
    