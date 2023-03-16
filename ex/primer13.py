# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


with open("file2.txt", "r") as fileptr:
    print("The filepointer is at byte: ", fileptr.tell())

    content = fileptr.read()

    print("After reading, the filepointer is af:", fileptr.tell())
