from tkinter import *
from tkinter import filedialog
import Algorithms
import Steganography
from Globals import Globals
from Steganography import Steganography
from Algorithms import Algorithms


class Display:
    def __init__(self):
        self.Globals = Globals()
        self.Steganography = Steganography()
        self.Algorithms = Algorithms()

        self.root = Tk()
        self.root.title(self.Globals.window_tittle)
        self.root.geometry(self.Globals.window_size)
        self.root.resizable(width=False, height=False)

        self.main_menu = Menu(self.root)
        self.algorithm_menu = Menu()
        self.steg_menu = Menu()

        self.showing_main_menu(self.main_menu)
        self.showing_algorithm_menu(self.algorithm_menu)
        self.showing_steg_menu(self.steg_menu)

        self.root.config(menu=self.main_menu)
        self.root.mainloop()

    def destroy_useless_items(self):
        """
        Удаление ненужных элементов интерфейса, для корректного отображения
        """
        for child in self.root.winfo_children():
            if not isinstance(child, Menu):
                child.destroy()

    def showing_main_menu(self, main_menu):
        """
        Отображение каскадного меню
        """
        main_menu.add_cascade(label="Алгоритмы", menu=self.algorithm_menu, activebackground=self.Globals.button_color)
        main_menu.add_cascade(label="Стеганография", menu=self.steg_menu, activebackground=self.Globals.button_color)

    def showing_algorithm_menu(self, algorithm_menu):
        """
        Отображение каскадного меню для шифрованию
        """
        algorithm_menu.add_command(label=f"{self.Globals.text_encrypt_tittle} {self.Globals.text_caesar}",
                                   activebackground=self.Globals.button_color,
                                   command=lambda: self.showing_main_menu_interface_encrypt(self.Globals.text_caesar,
                                                                                            0))

        algorithm_menu.add_command(label=f"{self.Globals.text_encrypt_tittle} {self.Globals.text_visener}",
                                   activebackground=self.Globals.button_color,
                                   command=lambda: self.showing_main_menu_interface_encrypt(self.Globals.text_visener,
                                                                                            1))

        algorithm_menu.add_command(label=f"{self.Globals.text_encrypt_tittle} {self.Globals.text_vernam}",
                                   activebackground=self.Globals.button_color, command=lambda:
            self.showing_main_menu_interface_encrypt(self.Globals.text_vernam, 2))

        algorithm_menu.add_command(label=f"{self.Globals.text_encrypt_tittle} {self.Globals.text_morse}",
                                   activebackground=self.Globals.button_color, command=lambda:
            self.showing_main_menu_interface_encrypt(self.Globals.text_morse, 3))

        algorithm_menu.add_separator()

        algorithm_menu.add_command(label=f"Дешифрование {self.Globals.text_caesar}",
                                   command=lambda: self.showing_main_menu_interface_decode(self.Globals.text_caesar, 0),
                                   activebackground=self.Globals.button_color)
        algorithm_menu.add_command(label=f"Дешифрование {self.Globals.text_visener}",
                                   activebackground=self.Globals.button_color,
                                   command=lambda: self.showing_main_menu_interface_decode(self.Globals.text_visener, 1))
        algorithm_menu.add_command(label=f"Дешифрование {self.Globals.text_vernam}", activebackground=self.Globals.button_color,
                                   command=lambda:
                                   self.showing_main_menu_interface_decode(self.Globals.text_vernam, 2))
        algorithm_menu.add_command(label=f"Дешифрование {self.Globals.text_morse}",
                                   activebackground=self.Globals.button_color,
                                   command=lambda: self.showing_main_menu_interface_decode(self.Globals.text_morse, 3))
        algorithm_menu.add_command(label=f"Дешифрование {self.Globals.text_count_morse}",
                                   activebackground=self.Globals.button_color,
                                   command=lambda: self.showing_main_menu_interface_decode(
                                       self.Globals.text_count_morse, 4))

    def showing_steg_menu(self, steg_menu):
        """
        Отображение каскадного меню для стеганографии
        """
        steg_menu.add_command(label="Внедрение в bmp", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_encrypt(self.Globals.text_bmp))
        steg_menu.add_command(label="Внедрение в jpg", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_encrypt(self.Globals.text_jpg))
        steg_menu.add_command(label="Внедрение в png", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_encrypt(self.Globals.text_png))

        steg_menu.add_separator()

        steg_menu.add_command(label="Извлечение из bmp", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_decode(self.Globals.text_bmp))
        steg_menu.add_command(label="Извлечение из jpg", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_decode(self.Globals.text_jpg))
        steg_menu.add_command(label="Извлечение из png", activebackground=self.Globals.button_color, command=lambda:
        self.showing_steg_menu_interface_decode(self.Globals.text_png))

    def showing_main_menu_interface_encrypt(self, encrypt_name, check_encrypt):
        """
        Отображение интерфейса для шифрования
        check_encrypt:
                    0 - шифрование Цезаря
                    1 - шифрование Виженера
                    2 - шифрование Вернама
                    3 - шифрование в Азбуку Морзе
        """
        self.destroy_useless_items()
        self.root.title(f"{self.Globals.text_encrypt_tittle} {encrypt_name}")

        input_way_label = StringVar()
        input_way_label.set("Путь до файла (Текст):")
        input_way = Entry(bd="4", width="40", textvariable=input_way_label)
        input_way.place(x=90, y=30)

        if check_encrypt in [0, 1, 2]:
            shift_input_way_label = StringVar()
            if check_encrypt == 0:
                shift_input_way_label.set("Сдвиг(-33:33):")
            else:
                shift_input_way_label.set("Ключ:")

            shift_input_way = Entry(bd="3", width="13", textvariable=shift_input_way_label)
            shift_input_way.place(x=90, y=66)

        choose_input_way = Button(text="Выбрать", activebackground=self.Globals.button_color, command=lambda:
        input_way_label.set(filedialog.askopenfilename()))
        choose_input_way.place(x=235, y=65)

        clear_input_way = Button(text="Удалить", activebackground=self.Globals.button_color, command=lambda:
        [input_way_label.set(""), shift_input_way_label.set("")])
        clear_input_way.place(x=335, y=65)

        if check_encrypt != 0:
            value_radiobutton = BooleanVar()
            value_radiobutton.set(0)
            rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
            en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
            rus_checkbutton.place(x=83, y=110)
            en_checkbutton.place(x=230, y=110)

        encrypt = Button()

        if check_encrypt == 0:
            encrypt = Button(text=self.Globals.text_encrypt_button, activebackground=self.Globals.button_color,
                             width="38", height="2",
                             command=lambda:
                             self.Algorithms.caesar_encryption(input_way.get(), shift_input_way.get()))
        elif check_encrypt == 1:
            encrypt = Button(text=self.Globals.text_encrypt_button, activebackground=self.Globals.button_color,
                             width="38", height="2",
                             command=lambda:
                             self.Algorithms.visener_encrtyption(input_way.get(), shift_input_way.get(), value_radiobutton.get(), 0))
        elif check_encrypt == 2:
            encrypt = Button(text=self.Globals.text_encrypt_button, activebackground=self.Globals.button_color,
                             width="38", height="2",
                             command=lambda:
                             self.Algorithms.vernam_encrtyption(input_way.get(), shift_input_way.get(),
                                                                value_radiobutton.get()))
        elif check_encrypt == 3:
            encrypt = Button(text=self.Globals.text_encrypt_button, activebackground=self.Globals.button_color,
                             width="38", height="2",
                             command=lambda:
                             self.Algorithms.morse_encrtyption(input_way.get(), value_radiobutton.get(), 0))

        encrypt.place(x=90, y=150)

    def showing_main_menu_interface_decode(self, decode_name, check_decode):
        """
        Отображение интерфейса для дешифрования
        check_decode:
            0 - дешифрование Цезаря
            1 - дешифрование Виженера
            2 - дешифрование Вернама
            3 - дешифрование из Азбуки Морзе
            4 - дешифрование методом частотного анализа
        """
        self.destroy_useless_items()
        self.root.title(f"{self.Globals.text_decode_tittle} {decode_name}")

        input_way_label = StringVar()
        input_way_label.set("Путь до файла (Текст):")
        input_way = Entry(bd="4", width="40", textvariable=input_way_label)
        input_way.place(x=90, y=30)

        shift_input_way_label = StringVar()
        if check_decode in [0, 1, 2]:
            if check_decode == 0:
                shift_input_way_label.set("Сдвиг(-33:33):")
            else:
                shift_input_way_label.set("Ключ:")

            shift_input_way = Entry(bd="3", width="13", textvariable=shift_input_way_label)
            shift_input_way.place(x=90, y=66)

        choose_input_way = Button(text="Выбрать", activebackground=self.Globals.button_color, command=lambda:
        input_way_label.set(filedialog.askopenfilename()))
        choose_input_way.place(x=235, y=65)

        clear_input_way = Button(text="Удалить", activebackground=self.Globals.button_color, command=lambda:
                                [input_way_label.set(""), shift_input_way_label.set("")])
        clear_input_way.place(x=335, y=65)

        if check_decode != 0:
            value_radiobutton = BooleanVar()
            value_radiobutton.set(0)
            rus_checkbutton = Radiobutton(text="Русский", variable=value_radiobutton, value=1)
            en_checkbutton = Radiobutton(text="Английский", variable=value_radiobutton, value=0)
            rus_checkbutton.place(x=83, y=110)
            en_checkbutton.place(x=230, y=110)

        decode = Button()

        if check_decode == 0:
            decode = Button(text=self.Globals.text_decode_button, activebackground=self.Globals.button_color,
                            width="38", height="2",
                            command=lambda:
                            self.Algorithms.caesar_encryption(input_way.get(), "-" + shift_input_way.get()))
        elif check_decode == 1:
            decode = Button(text=self.Globals.text_decode_button, activebackground=self.Globals.button_color,
                            width="38", height="2",
                            command=lambda:
                            self.Algorithms.visener_encrtyption(input_way.get(), shift_input_way.get(), value_radiobutton.get(), 1))
        elif check_decode == 2:
            decode = Button(text=self.Globals.text_decode_button, activebackground=self.Globals.button_color,
                            width="38", height="2",
                            command=lambda:
                            self.Algorithms.vernam_encrtyption(input_way.get(), shift_input_way.get(),
                                                               value_radiobutton.get(), 1))
        elif check_decode == 3:
            decode = Button(text=self.Globals.text_decode_button, activebackground=self.Globals.button_color,
                            width="38", height="2",
                            command=lambda:
                            self.Algorithms.morse_encrtyption(input_way.get(), value_radiobutton.get(), 1))
        elif check_decode == 4:
            decode = Button(text=self.Globals.text_decode_button, activebackground=self.Globals.button_color,
                            width="38", height="2",
                            command=lambda:
                            self.Algorithms.caesar_partial_analysis_encrtyption(input_way.get(),
                                                                                value_radiobutton.get(), 1))

        decode.place(x=90, y=150)

    def showing_steg_menu_interface_encrypt(self, type_of_file):
        """
        Отображение интерфейса для кодирования в изображение
        """
        self.destroy_useless_items()
        self.root.title(f"{self.Globals.text_incode_img} {type_of_file}")

        input_way_label = StringVar()
        input_way_label.set(f"Путь до картинки (.{type_of_file}):")
        input_way = Entry(bd="4", width="40", textvariable=input_way_label)
        input_way.place(x=90, y=30)

        message_label = StringVar()
        message_label.set("Сообщение:")
        message = Entry(bd="3", width="13", textvariable=message_label)
        message.place(x=90, y=66)

        choose_input_way = Button(text="Выбрать", activebackground=self.Globals.button_color, command=lambda:
        input_way_label.set(filedialog.askopenfilename()))
        choose_input_way.place(x=235, y=65)

        clear_input_way = Button(text="Удалить", activebackground=self.Globals.button_color, command=lambda:
        [input_way_label.set(""), message_label.set("")])
        clear_input_way.place(x=335, y=65)

        encrypt = Button(text=self.Globals.text_incode_img, activebackground=self.Globals.button_color, width="38",
                         height="2",
                         command=lambda:
                         self.Steganography.encode(input_way_label.get(), message_label.get()))

        encrypt.place(x=90, y=150)

    def showing_steg_menu_interface_decode(self, type_of_file):
        """
        Отображение интерфейса для декодирования из изображения
        """
        self.destroy_useless_items()
        self.root.title(f"{self.Globals.text_decode_img} {type_of_file}")

        input_way_label = StringVar()
        input_way_label.set(f"Путь до картинки (.{type_of_file}):")
        input_way = Entry(bd="4", width="40", textvariable=input_way_label)
        input_way.place(x=90, y=30)

        choose_input_way = Button(text="Выбрать", activebackground=self.Globals.button_color, command=lambda:
        input_way_label.set(filedialog.askopenfilename()))
        choose_input_way.place(x=235, y=65)

        clear_input_way = Button(text="Удалить", activebackground=self.Globals.button_color, command=lambda:
        input_way_label.set(""))
        clear_input_way.place(x=335, y=65)

        encrypt = Button(text=self.Globals.text_decode_img, activebackground=self.Globals.button_color, width="38",
                         height="2",
                         command=lambda:
                         self.Steganography.decode(input_way_label.get()))

        encrypt.place(x=90, y=150)
