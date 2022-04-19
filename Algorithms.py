from tkinter import *
from tkinter import messagebox, Toplevel


def error():
    messagebox.showwarning(message="Что-то пошло не так, попробуйте заново!")


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


def visiner_encryption(way_to_file, key, language, flag=""):
    pass


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

                copy_text_input_window = Button(input_window, text="Скопировать", activebackground="grey", command=lambda:
                                                input_window.clipboard_append(result_string))
                copy_text_input_window.place(x=1, y=50)
            except Exception:
                error()
                return

    input_window.geometry("800x300")
    input_window.mainloop()
