from tkinter import messagebox


def caesar_encryption(way_to_file, shift):
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
                if en_alphabet.index(i) < 25:
                    result_string += en_alphabet[en_alphabet.index(i) + shift]
                else:
                    result_string += en_alphabet[en_alphabet.index(i) + shift]
            elif i in rus_alphabet:
                if rus_alphabet.index(i) < 33:
                    result_string += rus_alphabet[rus_alphabet.index(i) + shift]
                else:
                    result_string += rus_alphabet[rus_alphabet.index(i) + shift]
            elif i in numbers:
                result_string += str((int(numbers[numbers.index(i)]) + shift) % 10)
            else:
                result_string += i

        point_index = way_to_file.rfind('.')
        new_way_mod_file = way_to_file[:point_index]+'_modified'+way_to_file[point_index:]
        open(new_way_mod_file, "w+").write(result_string)
        messagebox.showinfo('', f'Итог: {result_string} \n\n Путь к новому файлу: {new_way_mod_file}')

    except Exception:

        try:
            shift = int(shift)
            for i in way_to_file:
                if i in en_alphabet:
                    if en_alphabet.index(i) < 25:
                        result_string += en_alphabet[en_alphabet.index(i) + shift]
                    else:
                        result_string += en_alphabet[en_alphabet.index(i) + shift]
                elif i in rus_alphabet:
                    if rus_alphabet.index(i) < 33:
                        result_string += rus_alphabet[rus_alphabet.index(i) + shift]
                    else:
                        result_string += rus_alphabet[rus_alphabet.index(i) + shift]
                elif i in numbers:
                    result_string += str((int(numbers[numbers.index(i)]) + shift) % 10)
                else:
                    result_string += i

            messagebox.showinfo('', f'{result_string}')

        except Exception:
            messagebox.showwarning(message="Что-то пошло не так, попробуй заново!")


