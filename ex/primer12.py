# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as fileptr:
        sentences = f.readlines()

    for sentence in sentences:
        if "," in sentence:
            print(sentence)