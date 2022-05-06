from tkinter import *
from tkinter import messagebox, Toplevel
from Globals import Globals
import traceback


class Algorithms:
    def __init__(self):
        self.Globals = Globals()

    def error(self, message="Что-то пошло не так, попробуйте заново!"):
        """
        Вывод ошибки в данных пользователя
        """
        messagebox.showwarning(message)

    def get_new_way_to_mod_file(self, way_to_file, result_string):
        """
        Создание и вывод нового файла для зашифрованных файлов
        """
        point_index = way_to_file.rfind('.')
        new_way_mod_file = way_to_file[:point_index] + '_modified' + way_to_file[point_index:]
        open(new_way_mod_file, "w+").write(result_string)
        return new_way_mod_file

    def out_put_of_result(self, result_string, new_way_mod_file=False):
        """
        Вывод шифрования или дешифрования
        """
        output_window = Toplevel()
        text_output_window = Label()

        if new_way_mod_file:
            text_output_window = Label(output_window,
                                       text=f"Итог: {result_string}\n\nПуть до зашифрованного файла: {new_way_mod_file}")
        else:
            text_output_window = Label(output_window, text=f"Итог: {result_string}")

        text_output_window.place(x=1, y=1)
        copy_text_output_window = Button(output_window, text="Скопировать", activebackground="grey",
                                         command=lambda: output_window.clipboard_append(result_string))
        copy_text_output_window.place(x=1, y=70)

        output_window.geometry("800x300")
        output_window.mainloop()

    def caesar_encryption(self, way_to_file, shift):
        """
        Шифрование Цезаря
        """
        numbers = self.Globals.numbers
        en_alphabet = self.Globals.en_alphabet
        EN_alphabet = self.Globals.EN_alphabet

        rus_alphabet = self.Globals.rus_alphabet
        RUS_alphabet = self.Globals.RUS_alphabet
        result_string = ''

        try:
            shift = int(shift)
            text_from_file = open(way_to_file, "r").read()
            for i in text_from_file:
                if i in en_alphabet:
                    result_string += en_alphabet[(en_alphabet.index(i) + shift) % len(en_alphabet)]
                elif i in EN_alphabet:
                    result_string += EN_alphabet[(EN_alphabet.index(i) + shift) % len(EN_alphabet)]
                elif i in rus_alphabet:
                    result_string += rus_alphabet[(rus_alphabet.index(i) + shift) % len(rus_alphabet)]
                elif i in RUS_alphabet:
                    result_string += rus_alphabet[(rus_alphabet.index(i) + shift) % len(rus_alphabet)]
                elif i in numbers:
                    shift_num = shift % 10
                    result_string += str((int(numbers[numbers.index(i)]) + shift_num) % 10)
                else:
                    result_string += i

            new_way_mod_file = self.get_new_ay_to_mod_file(way_to_file, result_string)
            self.out_put_of_result(result_string, new_way_mod_file)

        except Exception:

            try:
                shift = int(shift)
                for i in way_to_file:
                    if i in en_alphabet:
                        result_string += en_alphabet[(en_alphabet.index(i) + shift) % len(en_alphabet)]
                    elif i in EN_alphabet:
                        result_string += EN_alphabet[(EN_alphabet.index(i) + shift) % len(EN_alphabet)]
                    elif i in rus_alphabet:
                        result_string += rus_alphabet[(rus_alphabet.index(i) + shift) % len(rus_alphabet)]
                    elif i in RUS_alphabet:
                        result_string += RUS_alphabet[(RUS_alphabet.index(i) + shift) % len(RUS_alphabet)]
                    elif i in numbers:
                        shift_num = shift % 10
                        result_string += str((int(numbers[numbers.index(i)]) + shift_num) % 10)
                    else:
                        result_string += i

                self.out_put_of_result(result_string)

            except Exception as exc:
                self.error()

    def morse_encrtyption(self, way_to_file, language=0, check_decoder=0):
        """
        Шифрование/дешифрование Азбукой Морзе
        """
        symbol = self.Globals.symbol
        result_string = ''

        symbol_keys = list(symbol.keys())
        symbol_values = list(symbol.values())

        if check_decoder == 1:
            try:

                text_from_file = open(way_to_file, "r").read().lower()
                print("fbr")
                for i in text_from_file.split(" "):
                    print(i)
                    result_string += symbol_keys[symbol_values.index(i)] + " "
                print(result_string)
                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

            except Exception as exc:
                print(traceback.format_exc())
                try:
                    for i in way_to_file.split(' '):
                        result_string += symbol_keys[symbol_values.index(i)]

                    self.out_put_of_result(result_string)

                except Exception as exc:
                    print(exc)
                    self.error()

        else:
            try:
                text_from_file = open(way_to_file, "r").read().lower()

                for i in text_from_file:
                    result_string += symbol[i] + " "

                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

            except Exception:

                try:
                    for i in way_to_file.lower():
                        result_string += symbol[i] + " "

                    self.out_put_of_result(result_string)

                except Exception:
                    self.error()

    def caesar_partial_analysis_encrtyption(self, way_to_file, language=0):
        """
        Дешифрование шифра Цезаря методом частотного анализа
        """
        numbers = self.Globals.numbers

        en_alphabet = self.Globals.en_alphabet
        EN_alphabet = self.Globals.EN_alphabet

        rus_alphabet = self.Globals.rus_alphabet
        RUS_alphabet = self.Globals.RUS_alphabet

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
                if i in en_alphabet:
                    result_string += en_alphabet[(en_alphabet.index(i) - shift) % len(en_alphabet)]
                elif i in EN_alphabet:
                    result_string += EN_alphabet[(EN_alphabet.index(i) - shift) % len(EN_alphabet)]
                elif i in rus_alphabet:
                    result_string += rus_alphabet[(rus_alphabet.index(i) - shift) % len(rus_alphabet)]
                elif i in RUS_alphabet:
                    result_string += RUS_alphabet[(RUS_alphabet.index(i) - shift) % len(RUS_alphabet)]
                elif i in numbers:
                    shift_num = shift % 10
                    result_string += str((int(numbers[numbers.index(i)]) - shift_num) % 10)
                else:
                    result_string += i

            new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
            self.out_put_of_result(result_string, new_way_mod_file)

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
                    if i in en_alphabet:
                        result_string += en_alphabet[(en_alphabet.index(i) - shift) % len(en_alphabet)]
                    elif i in EN_alphabet:
                        result_string += EN_alphabet[(EN_alphabet.index(i) - shift) % len(EN_alphabet)]
                    elif i in rus_alphabet:
                        result_string += rus_alphabet[(rus_alphabet.index(i) - shift) % len(rus_alphabet)]
                    elif i in RUS_alphabet:
                        result_string += RUS_alphabet[(RUS_alphabet.index(i) - shift) % len(RUS_alphabet)]
                    elif i in numbers:
                        shift_num = shift % 10
                        result_string += str((int(numbers[numbers.index(i)]) - shift_num) % 10)
                    else:
                        result_string += i

                self.out_put_of_result(result_string)

            except Exception:
                self.error()

    def visener_encrtyption(self, way_to_file, key, language=0, check_decode=0):
        """
        Шифрование/дешифрование Виженера
        """
        result_string = ""

        if language == 0:
            alphabet = self.Globals.EN_alphabet
        else:
            alphabet = self.Globals.RUS_alphabet
        key = key.upper()

        if check_decode == 1:
            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                text_from_file = open(way_to_file, "r").read().upper()

                for i in range(len(text_from_file)):
                    result_string += alphabet[
                        (alphabet.index(text_from_file[i]) - (1 + alphabet.index(key[i % len(key)]))) % len(alphabet)]

                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

            except Exception:

                try:
                    for i in key:
                        if i not in alphabet:
                            raise Exception

                    for i in range(len(way_to_file)):
                        result_string += alphabet[
                            (alphabet.index(way_to_file[i]) - (1 + alphabet.index(key[i % len(key)]))) % len(alphabet)]

                    self.out_put_of_result(result_string)

                except Exception:
                    self.error()
        else:
            try:
                for i in key:
                    if i not in alphabet:
                        raise Exception

                text_from_file = open(way_to_file, "r").read().upper()

                for i in range(len(text_from_file)):
                    result_string += alphabet[
                        (alphabet.index(text_from_file[i]) + (1 + alphabet.index(key[i % len(key)]))) % len(alphabet)]

                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

            except Exception as exc:

                try:
                    for i in key:
                        if i not in alphabet:
                            raise Exception

                    for i in range(len(way_to_file)):
                        result_string += alphabet[
                            (alphabet.index(way_to_file[i]) + (1 + alphabet.index(key[i % len(key)]))) % len(alphabet)]

                    self.out_put_of_result(result_string)

                except Exception:
                    self.error()

    def vernam_encrtyption(self, way_to_file, key, language=0, check_decode=0):
        """
        Шифрование/Дешифрование Вернама
        """
        result_string = ""

        if language == 0:
            alphabet = self.Globals.EN_alphabet
        else:
            alphabet = self.Globals.RUS_alphabet
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
                    result_string += alphabet[
                        ((alphabet.index(text_from_file[i]) + 1) ^ (alphabet.index(key[i]) + 1)) % len(alphabet)]

                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

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

                    self.out_put_of_result(result_string)

                except Exception:
                    self.error()
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
                    result_string += alphabet[
                        ((alphabet.index(text_from_file[i]) + 1) ^ (alphabet.index(key[i]) + 1)) % len(alphabet)]

                new_way_mod_file = self.get_new_way_to_mod_file(way_to_file, result_string)
                self.out_put_of_result(result_string, new_way_mod_file)

            except Exception as exc:
                try:
                    for i in key:
                        if i not in alphabet:
                            raise Exception

                    if len(key) < len(way_to_file):
                        raise Exception

                    for i in range(len(way_to_file)):
                        result_string += alphabet[
                            ((alphabet.index(way_to_file[i]) + 1) ^ (alphabet.index(key[i]) + 1)) % len(alphabet)]

                    self.out_put_of_result(result_string)

                except Exception as exc:
                    self.error()
