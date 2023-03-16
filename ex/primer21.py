# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


import sys


if __name__ == "__mail__":
    for idx, arg in enumerate(sys.argv):
        print(f"Argument #{idx} is {arg}")
    print("No. of arguments passed is ", len(sys.argv))