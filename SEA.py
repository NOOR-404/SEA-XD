#!/data/data/com.termux/files/usr/bin/python3.13
# -*- coding: utf-8 -*-
import os
import subprocess
 
bit = os.uname().machine
changes = subprocess.getoutput("git status --porcelain")
 
if changes:
    os.system("git reset --hard")
    os.system("git clean -fd")
    os.system("git pull")
 
os.system("chmod 777 *")
 
if '64' in bit:
    import SEA
else:
    os.system("clear" if os.name == "posix" else "cls")
    print("TOOL NOT AVAILABLE FOR 32 BIT DEVICE")
