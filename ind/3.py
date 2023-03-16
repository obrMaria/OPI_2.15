#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    # Создание директории и запоминание пути
    new_dir = input("Введите имя директории: ")
    os.mkdir(new_dir)
    print(os.getcwd())

    # создание нового файла
    with open("newfile.txt", "x") as f:
        print(f)
        if f:
            print("File created successfully")

    # Переименование файла
    os.rename("newfile.txt", "my_file.txt")
