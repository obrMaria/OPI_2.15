#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и выводит
на экран только предложения, содержащие введенное с клавиатуры слово.
"""

if __name__ == "__main__":
    with open("1.txt", "r", encoding="utf-8") as file:
        sentences = file.read()

    word = input("введите слово ")

    # Вывод предложений с заданным словом.
    for sentence in sentences.split("\n"):
        if word in sentence:
            print(sentence)
