import cv2
import numpy as np
from tkinter import *
from tkinter import Toplevel


def to_bin(data):
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError()


def encode(image_name, secret_data):
    image = cv2.imread(image_name)
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    if len(secret_data) > n_bytes:
        raise ValueError
    secret_data += "====="
    data_index = 0
    binary_secret_data = to_bin(secret_data)
    data_len = len(binary_secret_data)
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break

    point_index = image_name.rfind('.')
    new_way_mod_file = image_name[:point_index] + '_modified' + image_name[point_index:]
    cv2.imwrite(new_way_mod_file, image)


def decode(image_name):
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break

    output_window = Toplevel()
    text_input_window = Label(output_window, text=f"Итог: {decoded_data[0:-5]}")
    text_input_window.place(x=1, y=1)

    copy_text_input_window = Button(output_window, text="Скопировать", activebackground="grey",
                                    command=lambda:
                                    output_window.clipboard_append(decoded_data[0:-5]))
    copy_text_input_window.place(x=1, y=50)

    output_window.geometry("800x300")
    output_window.mainloop()