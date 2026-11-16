import subprocess
import random
import sys
import string

def ask(message,function,param=None):
    print(message)
    response = input()
    if response == "yes":
        if param is None:
           function()
        else:
            function(param)
    else:
        print("Question Lost.. Moving On.")
        

def multi_line():
    inputofuser = "CANCEL"
    while "CANCEL" in inputofuser:
        print("====> ENTER TEXT <====")
        print("Do you want to save?/nCNTRL + D")
        print("++++++++++ CLOSING LINE ++++++++++")
        result = sys.stdin.read()
        if "CANCEL" in inputofuser:
            print("Canceling now..")
    return inputofuser
    

def add_a_user():
     print("Enter the users that you want to add.")
     usernames = multi_line().splitlines()
     for user in usernames:
         subprocess.run(f"sudo adduser --gecos \"\" --disabled-password {user}", shell = True)
         password = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))
         subprocess.run(f"echo \"{user}:{password}\" |chpasswd", shell = True)
         print(f"{user}: {password}")