from tkinter import *
from tkinter import filedialog
import Algorithms

root = Tk()


def destroy_useless_items():
    for child in root.winfo_children():
        if not isinstance(child, Menu):
            child.destroy()


def showing_caesar(name1, name2, flag=""):
    destroy_useless_items()
    root.title(f"{name1} Цезаря")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла (Текст):")
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

    encrypt = Button(text=name2, activebackground="grey", width="38", height="2", command=lambda:
                     Algorithms.caesar_encryption(input_way.get(), flag + shift_input_way.get()))
    encrypt.place(x=90, y=150)


def showing_visener(name1, name2, flag=''):
    destroy_useless_items()
    root.title(f"{name1} Виженера")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла (Текст):")
    input_way = Entry(bd="4", width="40", textvariable=input_way_label)
    input_way.place(x=90, y=30)

    key_input_way_label = StringVar()
    key_input_way_label.set("Ключ:")
    key_input_way = Entry(bd="3", width="13", textvariable=key_input_way_label)
    key_input_way.place(x=90, y=66)

    choose_input_way = Button(text="Выбрать", activebackground="grey", command=lambda:
                              input_way_label.set(filedialog.askopenfilename()))
    choose_input_way.place(x=235, y=65)

    clear_input_way = Button(text="Удалить", activebackground="grey", command=lambda:
                             [input_way_label.set(""), key_input_way_label.set("")])
    clear_input_way.place(x=335, y=65)

    value_radiobutton = BooleanVar()
    value_radiobutton.set(0)
    rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
    en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
    rus_checkbutton.place(x=83, y=110)
    en_checkbutton.place(x=230, y=110)

    encrypt = Button(text=name2, activebackground="grey", width="38", height="2",
                     command=Algorithms.visiner_encryption(input_way.get(), key_input_way.get(), value_radiobutton.get()))
    encrypt.place(x=90, y=150)


def showing_vernam(name1, name2):
    destroy_useless_items()
    root.title(f"{name1} Вернама")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла (Текст):")
    input_way = Entry(bd="4", width="40", textvariable=input_way_label)
    input_way.place(x=90, y=30)

    key_input_way_label = StringVar()
    key_input_way_label.set("Ключ:")
    key_input_way = Entry(bd="3", width="13", textvariable=key_input_way_label)
    key_input_way.place(x=90, y=66)

    choose_input_way = Button(text="Выбрать", activebackground="grey", command=lambda:
                              input_way_label.set(filedialog.askopenfilename()))
    choose_input_way.place(x=235, y=65)

    clear_input_way = Button(text="Удалить", activebackground="grey", command=lambda:
                             [input_way_label.set(""), key_input_way_label.set("")])
    clear_input_way.place(x=335, y=65)

    value_radiobutton = BooleanVar()
    value_radiobutton.set(0)
    rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
    en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
    rus_checkbutton.place(x=83, y=110)
    en_checkbutton.place(x=230, y=110)

    encrypt = Button(text=name2, activebackground="grey", width="38", height="2",
                     command=Algorithms.visiner_encryption(input_way.get(), key_input_way.get(), value_radiobutton.get()))
    encrypt.place(x=90, y=150)


def showing_morse(name1, name2, check_decoder=0):
    destroy_useless_items()
    root.title(f"{name1} Азбуки Морзе")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла (Текст):")
    input_way = Entry(bd="4", width="40", textvariable=input_way_label)
    input_way.place(x=90, y=30)

    choose_input_way = Button(text="Выбрать", activebackground="grey", command=lambda:
                              input_way_label.set(filedialog.askopenfilename()))
    choose_input_way.place(x=235, y=65)

    clear_input_way = Button(text="Удалить", activebackground="grey", command=lambda:
                             input_way_label.set(""))
    clear_input_way.place(x=335, y=65)

    value_radiobutton = BooleanVar()
    value_radiobutton.set(0)
    rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
    en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
    rus_checkbutton.place(x=83, y=110)
    en_checkbutton.place(x=230, y=110)

    encrypt = Button(text=name2, activebackground="grey", width="38", height="2",
                     command=lambda: Algorithms.morse_encrtyption(input_way.get(), value_radiobutton.get(), check_decoder))
    encrypt.place(x=90, y=150)


def showing_caesar_partial_analysis(name1, name2):
    destroy_useless_items()
    root.title(f"{name1} Морзе частотным анализом")

    input_way_label = StringVar()
    input_way_label.set("Путь до файла (Текст):")
    input_way = Entry(bd="4", width="40", textvariable=input_way_label)
    input_way.place(x=90, y=30)

    choose_input_way = Button(text="Выбрать", activebackground="grey", command=lambda:
                              input_way_label.set(filedialog.askopenfilename()))
    choose_input_way.place(x=235, y=65)

    clear_input_way = Button(text="Удалить", activebackground="grey", command=lambda:
                             input_way_label.set(""))
    clear_input_way.place(x=335, y=65)

    value_radiobutton = BooleanVar()
    value_radiobutton.set(0)
    rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
    en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
    rus_checkbutton.place(x=83, y=110)
    en_checkbutton.place(x=230, y=110)

    encrypt = Button(text=name2, activebackground="grey", width="38", height="2",
                     command=lambda: Algorithms.caesar_partial_analysis_encrtyption(input_way.get(), value_radiobutton.get()))
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

    algorithm_menu.add_command(label="Шифрование Цезаря",
                               command=lambda: showing_caesar("Шифрование", "Зашифровать"), activebackground="grey")
    algorithm_menu.add_command(label="Шифрование Виженера", activebackground="grey",
                               command=lambda: showing_visener('Шифрование', 'Зашифровать', ''))
    algorithm_menu.add_command(label="Шифрование Вернама", activebackground="grey", command=lambda:
                               showing_vernam("Шифрование", "Зашифровать"))
    algorithm_menu.add_command(label="Шифрование Азбуки Морзе", activebackground="grey", command=lambda:
                               showing_morse("Шифрование", "Зашифровать"))
    algorithm_menu.add_separator()
    algorithm_menu.add_command(label="Дешифрование Цезаря",
                               command=lambda: showing_caesar("Дешифрование", "Дешифровать", "-"),
                               activebackground="grey")
    algorithm_menu.add_command(label="Дешифрование Виженера",
                               activebackground="grey",
                               command=lambda: showing_visener('Дешифрование', 'Дешифровать', ''))
    algorithm_menu.add_command(label="Дешифрование Вернама", activebackground="grey", command=lambda:
                               showing_vernam("Дешифрование", "Дешифровать"))
    algorithm_menu.add_command(label="Дешифрование Цезаря частотным анализом",
                               activebackground="grey",
                               command=lambda: showing_caesar_partial_analysis("Дешифрование", "Дешифровать"))
    algorithm_menu.add_command(label="Дешифрование Азбуки Морзе",
                               activebackground="grey",
                               command=lambda: showing_morse("Дешифрование", "Дешифровать", 1))

    steg_menu.add_command(label="Внедрение в bmp", activebackground="grey")
    steg_menu.add_command(label="Внедрение в jpg", activebackground="grey")
    steg_menu.add_command(label="Внедрение в png", activebackground="grey")
    steg_menu.add_separator()
    steg_menu.add_command(label="Извлечение из bmp", activebackground="grey")
    steg_menu.add_command(label="Извлечение из jpg", activebackground="grey")
    steg_menu.add_command(label="Извлечение из png", activebackground="grey")

    root.config(menu=main_menu)
    root.mainloop()
