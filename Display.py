from tkinter import *

def caesar_encryption():
    pass



class Display():
    root = Tk()
    root.title("Шифратор")
    root.geometry("1000x800")

    main_menu = Menu(root)
    algorithm_menu = Menu()
    steg_menu = Menu()

    main_menu.add_cascade(label="Алгоритмы", menu=algorithm_menu)
    main_menu.add_cascade(label="Стеганография", menu=steg_menu)

    algorithm_menu.add_command(label="Шифрование Цезаря", command=)
    algorithm_menu.add_command(label="Шифрование Виженера")
    algorithm_menu.add_command(label="Шифрование Вернама")
    algorithm_menu.add_command(label="Шифрование Азбуки Морзе")
    algorithm_menu.add_separator()
    algorithm_menu.add_command(label="Дешифрование Цезаря")
    algorithm_menu.add_command(label="Дешифрование Виженера")
    algorithm_menu.add_command(label="Дешифрование Вернама")
    algorithm_menu.add_command(label="Дешифрование Азбуки Морзе")

    steg_menu.add_command(label="Внедрение в bmp")
    steg_menu.add_command(label="Внедрение в jpg")
    steg_menu.add_command(label="Внедрение в png")
    steg_menu.add_separator()
    steg_menu.add_command(label="Извлечение из bmp")
    steg_menu.add_command(label="Извлечение из jpg")
    steg_menu.add_command(label="Извлечение из png")

    root.config(menu=main_menu)
    root.mainloop()
