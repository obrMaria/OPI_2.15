# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


with open("newfile.txt", "x") as fileptr:
    print(fileptr)

    if fileptr:
        print("File created successfully")