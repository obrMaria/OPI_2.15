import sys

if __name__ == "__main__":
    for path in sys.argv:
        k = 0
        f = False
        try:
            file = open(path)
        except IOError as e:
            print('Не удалось открыть файл с именем ', path)
        else:

                text=sys.argv[1]:
                    text = file.read()
                    text = text.replace("\n", " ")
                    text = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "")
                    word = text.lower()
                    word = ''.join(filter(lambda x: x.isalpha(), word))
                    print(word)

                    c = {}

                    for letter in word:
                        c[letter] = c.get(letter, 0) + 1
                        sorted_c = {k: v for k, v in sorted(c.items(), key=lambda item: item[1])}

                    print(sorted_c)
