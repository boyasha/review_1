from tkinter import *
from tkinter import messagebox, Toplevel


def error():
    messagebox.showwarning(message="Что-то пошло не так, попробуйте заново!")


def get_new_way_to_mod_file(way_to_file, result_string):
    point_index = way_to_file.rfind('.')
    new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
    open(new_way_mod_file, "w+").write(result_string)


def caesar_encryption(way_to_file, shift, flag=""):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    en_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
                    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
                    'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    result_string = ''

    try:
        shift = int(shift)
        text_from_file = open(way_to_file, "r").read()
        for i in text_from_file:
            if i in en_alphabet:
                shift_en = shift % 26
                if en_alphabet.index(i) < 26:
                    result_string += en_alphabet[en_alphabet.index(i) + shift_en]
                else:
                    result_string += en_alphabet[en_alphabet.index(i) + shift_en]
            elif i in rus_alphabet:
                shift_rus = shift % 33
                if rus_alphabet.index(i) < 33:
                    result_string += rus_alphabet[rus_alphabet.index(i) + shift_rus]
                else:
                    result_string += rus_alphabet[rus_alphabet.index(i) + shift_rus]
            elif i in numbers:
                shift_num = shift % 10
                result_string += str((int(numbers[numbers.index(i)]) + shift_num) % 10)
            else:
                result_string += i

        if shift < 0:
            result_string = result_string.swapcase()

        point_index = way_to_file.rfind('.')
        new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
        open(new_way_mod_file, "w+").write(result_string)

        result_string += f"\n\n f{new_way_mod_file}"

    except Exception:

        try:
            shift = int(shift)
            for i in way_to_file:
                if i in en_alphabet:
                    shift_en = shift % 26
                    if en_alphabet.index(i) < 26:
                        result_string += en_alphabet[en_alphabet.index(i) + shift_en]
                    else:
                        result_string += en_alphabet[en_alphabet.index(i) + shift_en]
                elif i in rus_alphabet:
                    shift_rus = shift % 33
                    if rus_alphabet.index(i) < 33:
                        result_string += rus_alphabet[rus_alphabet.index(i) + shift_rus]
                    else:
                        result_string += rus_alphabet[rus_alphabet.index(i) + shift_rus]
                elif i in numbers:
                    shift_num = shift % 10
                    result_string += str((int(numbers[numbers.index(i)]) + shift_num) % 10)
                else:
                    result_string += i

            if shift < 0:
                result_string = result_string.swapcase()

        except Exception:
            error()


def morse_encrtyption(way_to_file, language=0, check_decoder=0):
    input_window = Toplevel()
    symbol = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        " ": " ",
        ".": "......",
        ",": ".-.-.-",
        "?": "..--..",
        "!": "--..--",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "а": ".-",
        "б": "-...",
        "в": ".--",
        "г": "--.",
        "д": "-..",
        "е": ".",
        "ё": ".",
        "ж": "...-",
        "з": "--..",
        "и": "..",
        "й": ".---",
        "к": "-.-",
        "л": ".-..",
        "м": "--",
        "н": "-.",
        "о": "---",
        "п": ".--.",
        "р": ".-.",
        "с": "...",
        "т": "-",
        "у": "..-",
        "ф": "..-.",
        "х": "....",
        "ц": "-.-.",
        "ч": "---.",
        "ш": "----",
        "щ": "--.-",
        "ь": "-..-",
        "ъ": "-..-",
        "ы": "-.--",
        "э": "..-..",
        "ю": "..__",
        "я": ".-.-",
    }
    result_string = ''

    if language == 1:
        symbol_keys = list(symbol.keys())[26:]
        symbol_values = list(symbol.values())[26:]
    else:
        symbol_keys = list(symbol.keys())[:41]
        symbol_values = list(symbol.values())[:41]

    if check_decoder == 1:
        try:
            text_from_file = open(way_to_file, "r").read().lower()

            for i in text_from_file.split(" "):
                result_string += symbol_keys[symbol_values.index(i)] + " "

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до дешифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)

        except Exception:

            try:
                for i in way_to_file.split(' '):
                    result_string += symbol_keys[symbol_values.index(i)] + " "

                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)



            except Exception as exc:
                print(exc)
                error()
                return

    else:
        try:
            text_from_file = open(way_to_file, "r").read().lower()

            for i in text_from_file:
                result_string += symbol[i] + " "

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)

        except Exception:

            try:
                for i in way_to_file.lower():
                    result_string += symbol[i] + " "
                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception:
                error()
                return

    input_window.geometry("800x300")
    input_window.mainloop()


def caesar_partial_analysis_encrtyption(way_to_file, language=0):
    input_window = Toplevel()
    result_string = ""

    if language == 1:
        popular_letter = 'о'
    else:
        popular_letter = 'e'

    try:
        text_from_file = open(way_to_file, "r").read().lower()
        count_letters = {}
        count_most_popular = 0
        for i in text_from_file:
            if i in count_letters.keys():
                count_letters[i] += 1
                if count_letters[i] > count_most_popular:
                    count_most_popular = count_letters[i]
            else:
                count_letters[i] = 0
        shift = ord(list(count_letters.keys())[list(count_letters.values()).index(count_most_popular)]) - ord(
            popular_letter)
        for i in text_from_file:
            if i == " ": continue
            result_string += chr(ord(i) - shift)
        point_index = way_to_file.rfind('.')
        new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
        open(new_way_mod_file, "w+").write(result_string)
        text_input_window = Label(input_window,
                                  text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
        text_input_window.place(x=1, y=1)
        copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
        input_window.clipboard_append(result_string))
        copy_text_input_window.place(x=1, y=70)
    except Exception:
        try:
            count_letters = {}
            count_most_popular = 0
            for i in way_to_file:
                if i in count_letters.keys():
                    count_letters[i] += 1
                    if count_letters[i] > count_most_popular:
                        count_most_popular = count_letters[i]
                else:
                    count_letters[i] = 0
            shift = ord(list(count_letters.keys())[list(count_letters.values()).index(count_most_popular)]) - ord(
                popular_letter)
            for i in way_to_file:
                if i == " ":
                    continue
                result_string += chr(ord(i) - shift)

            text_input_window = Label(input_window, text=f"Итог: {result_string}")
            text_input_window.place(x=1, y=1)
            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=50)
        except Exception:
            error()

    input_window.geometry("800x300")
    input_window.mainloop()


def visener_encrtyption(way_to_file, key, language=0, check_decode=0):
    input_window = Toplevel()
    result_string = ""

    if language == 0:
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    else:
        alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
                    'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    key = key.upper()

    if check_decode == 1:
        try:
            for i in key:
                if i not in alphabet:
                    raise Exception

            text_from_file = open(way_to_file, "r").read().upper()

            for i in range(len(text_from_file)):
                result_string += alphabet[
                    (alphabet.index(text_from_file[i]) - (alphabet.index(key[i % len(key)]))) % len(alphabet)]

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
                                            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)
        except Exception:

            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                for i in range(len(way_to_file)):
                    result_string += alphabet[
                        (alphabet.index(way_to_file[i]) - (alphabet.index(key[i % len(key)]))) % len(alphabet)]

                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception:
                error()
                return
    else:
        try:
            for i in key:
                if i not in alphabet:
                    raise Exception

            text_from_file = open(way_to_file, "r").read().upper()

            for i in range(len(text_from_file)):
                result_string += alphabet[
                    (alphabet.index(text_from_file[i]) + (alphabet.index(key[i % len(key)]))) % len(alphabet)]

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
                                            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)

        except Exception as exc:

            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                for i in range(len(way_to_file)):
                    result_string += alphabet[
                        (alphabet.index(way_to_file[i]) + (alphabet.index(key[i % len(key)]))) % len(alphabet)]

                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception:
                error()
                return

    input_window.geometry("800x300")
    input_window.mainloop()


def vernam_encrtyption(way_to_file, key, language=0, check_decode=0):
    input_window = Toplevel()
    result_string = ""

    if language == 0:
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    else:
        alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
                    'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    key = key.upper()

    if check_decode == 1:
        try:
            for i in key:
                if i not in alphabet:
                    raise Exception

            text_from_file = open(way_to_file, "r").read().upper()

            if len(key) < len(text_from_file):
                raise Exception

            for i in range(len(text_from_file)):
                result_string += alphabet[((alphabet.index(text_from_file[i])+1) ^ (alphabet.index(key[i])+1))%len(alphabet)]

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
                                            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)
        except Exception:

            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                if len(key) < len(way_to_file):
                    raise Exception

                for i in range(len(way_to_file)):
                    result_string += alphabet[
                        ((alphabet.index(way_to_file[i]) + 1) ^ (alphabet.index(key[i]) + 1)) % len(alphabet)]

                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception:
                error()
                return
    else:
        try:
            for i in key:
                if i not in alphabet:
                    raise Exception

            text_from_file = open(way_to_file, "r").read().upper()

            if len(key) < len(text_from_file):
                raise Exception

            if len(key) < len(text_from_file):
                raise Exception

            for i in range(len(text_from_file)):
                result_string += alphabet[((alphabet.index(text_from_file[i])+1) ^ (alphabet.index(key[i])+1))%len(alphabet)]

            point_index = way_to_file.rfind('.')
            new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
            open(new_way_mod_file, "w+").write(result_string)

            text_input_window = Label(input_window,
                                      text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
            text_input_window.place(x=1, y=1)

            copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
                                            input_window.clipboard_append(result_string))
            copy_text_input_window.place(x=1, y=70)

        except Exception as exc:
            print(exc)
            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                if len(key) < len(way_to_file):
                    raise Exception

                for i in range(len(way_to_file)):
                    result_string += alphabet[
                        ((alphabet.index(way_to_file[i]) + 1) ^ (alphabet.index(key[i]) + 1)) % len(alphabet)]

                text_input_window = Label(input_window, text=f"Итог: {result_string}")
                text_input_window.place(x=1, y=1)

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey",
                                                command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception as exc:
                print(exc)
                error()
                return

    input_window.geometry("800x300")
    input_window.mainloop()