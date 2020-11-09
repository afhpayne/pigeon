#!/bin/env python3

import os
import subprocess

cwd = os.getcwd()

directory_list = []

for directory in os.scandir(cwd):
    if os.path.isdir(directory) is True:
        directory_list.append(os.path.abspath(directory))
    directory_list.sort()
    
for directory in directory_list:
    if os.path.isdir((os.path.join(directory, ".git"))) is True:
        print("\n", str(directory.strip(" ")))
        pull_ok = input("'Enter' to pull or 's' to skip: ")
        if pull_ok == "s":
            pass
        else:
            subprocess.run(["git", "-C", directory, "pull"])
