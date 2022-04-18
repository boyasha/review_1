from tkinter import *
from tkinter import filedialog
import Algorithms

root = Tk()


def showing_caesar_encryption():
    root.title("Шифрование Цезаря")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла:")
    input_way = Entry(bd="4", width="40", textvariable=input_way_label)
    input_way.place(x=90, y=30)

    shift_input_way_label = StringVar()
    shift_input_way_label.set("Сдвиг(-33:33):")
    shift_input_way = Entry(bd="3", width="13", textvariable=shift_input_way_label)
    shift_input_way.place(x=90, y=66)

    choose_input_way = Button(text="Выбрать", activebackground="grey", command=lambda:
                              input_way_label.set(filedialog.askopenfilename()))
    choose_input_way.place(x=235, y=65)

    clear_input_way = Button(text="Удалить", activebackground="grey", command=lambda:
                             [input_way_label.set(""), shift_input_way_label.set("")])
    clear_input_way.place(x=335, y=65)

    encrypt = Button(text="Зашифровать", activebackground="grey", width="38", height="2", command=lambda:
                     Algorithms.caesar_encryption(input_way.get(), shift_input_way.get()))
    encrypt.place(x=90, y=150)


class Display:
    root.title("Шифратор")
    root.geometry("500x300")
    root.resizable(width=False, height=False)

    main_menu = Menu(root)
    algorithm_menu = Menu()
    steg_menu = Menu()

    main_menu.add_cascade(label="Алгоритмы", menu=algorithm_menu, activebackground="grey")
    main_menu.add_cascade(label="Стеганография", menu=steg_menu, activebackground="grey")

    algorithm_menu.add_command(label="Шифрование Цезаря", command=showing_caesar_encryption, activebackground="grey")
    algorithm_menu.add_command(label="Шифрование Виженера", command=showing_caesar_encryption, activebackground="grey")
    algorithm_menu.add_command(label="Шифрование Вернама", command=showing_caesar_encryption, activebackground="grey")
    algorithm_menu.add_command(label="Шифрование Азбуки Морзе", command=showing_caesar_encryption,
                               activebackground="grey")
    algorithm_menu.add_separator()
    algorithm_menu.add_command(label="Дешифрование Цезаря", command=showing_caesar_encryption, activebackground="grey")
    algorithm_menu.add_command(label="Дешифрование Виженера", command=showing_caesar_encryption,
                               activebackground="grey")
    algorithm_menu.add_command(label="Дешифрование Вернама", command=showing_caesar_encryption, activebackground="grey")
    algorithm_menu.add_command(label="Дешифрование Цезаря частотным анализом", command=showing_caesar_encryption,
                               activebackground="grey")
    algorithm_menu.add_command(label="Дешифрование Азбуки Морзе", command=showing_caesar_encryption,
                               activebackground="grey")

    steg_menu.add_command(label="Внедрение в bmp", command=showing_caesar_encryption, activebackground="grey")
    steg_menu.add_command(label="Внедрение в jpg", command=showing_caesar_encryption, activebackground="grey")
    steg_menu.add_command(label="Внедрение в png", command=showing_caesar_encryption, activebackground="grey")
    steg_menu.add_separator()
    steg_menu.add_command(label="Извлечение из bmp", command=showing_caesar_encryption, activebackground="grey")
    steg_menu.add_command(label="Извлечение из jpg", command=showing_caesar_encryption, activebackground="grey")
    steg_menu.add_command(label="Извлечение из png", command=showing_caesar_encryption, activebackground="grey")

    root.config(menu=main_menu)
    root.mainloop()
