import subprocess, re, sys, os, datetime, random, string, debianutils

def update():
    print("Initializing Updates..")
    subprocess.run("sudo apt update", shell = True)
    subprocess.run("sudo apt upgrade", shell = True)
        