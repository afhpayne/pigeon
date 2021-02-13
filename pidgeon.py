#!/usr/bin/env python3

# MIT License

# Copyright (c) 2020 afhpayne

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

# Software Name
soft_name = "Pidgeon"
soft_tag = "a simple script to update local git repositories"

# Version
soft_vers = "0.1.3"

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
