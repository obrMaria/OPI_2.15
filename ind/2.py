import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(
            "Передайте имя файла в качестве аргумента командной строки: ",
            sys.argv,
            len(sys.argv),
        )
        quit()

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            text = (f.readlines())

            k = 0
            text = ''.join(text)
            text = text.replace("\n", " ")
            text = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace(
                "!", "")
            word = text.lower()
            word = ''.join(filter(lambda x: x.isalpha(), word))
            print(word)

            c = {}

            for letter in word:
                c[letter] = c.get(letter, 0) + 1
                sorted_c = {k: v for k, v in sorted(c.items(), key=lambda item: item[1])}

            print(sorted_c)

    except IOError:
        # Отображаем ошибку, если с чтением из файла возникли проблемы
        print("Ошибка при доступе к файлу.")
