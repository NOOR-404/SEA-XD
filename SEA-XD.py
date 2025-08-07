import os
import subprocess
from os import system
G="\033[1;92m";W="\x1b[38;5;15m"
bit = os.uname().machine
changes = subprocess.getoutput('git status --porcelain')
if changes:system('git reset --hard');system('git clean -fd');system('git pull')
system('chmod 777 *')
if '64' in bit:
  import SEA
if "32" in bit:system('clear');print(f"{G}⊲[{W}●{G}]⊳{W} THIS TOOL NOT AVAILABLE FOR 32 BIT DEVICE...{G}!{W} ");print(f"{G}{54*'━'}")
