from os.path import exists
from pathlib import Path

# Example file path :- D:/APPLICATION DEVELOPMENT/Python-Progs/c-98/c-98.txt


def main():
    while True:
        input_file = str(
            raw_input(
                "Please enter the exact path of the file you wish to open :- ")
        )
        get_file(input_file)


def get_file(file_path):

    file_exists = exists(file_path)

    words_in_file = 0

    if(file_exists):

        path = Path(file_path)

        if (Path.is_file(path)):
            file_words = open(file_path, "r")

            file_lines = open(file_path).readlines()

            for file_line in file_lines:
                count_words_in_line(file_line)

            for file_word in file_words:
                _words = file_word.split()
                words_in_file = words_in_file + len(_words)

            print("Number of words in file are :- ", words_in_file)
        else:
            print("That is not a file.That is a folder")

    else:
        print("File / Folder doesn't exist.")


def count_words_in_line(_str):
    words = _str.split()

    print("Words in line :- ", words)
    print("Number of words in line :- ", len(words))


main()
