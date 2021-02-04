import tkinter as tk
import pyshorteners as ps


def short_link(user_link):
    link = ps.Shortener()
    short_link = link.tinyurl.short(user_link)
    return short_link

def clicked():
    link = url.get()
    ready_link = short_link(link)
    short_url.insert(0, ready_link)

def copy_link():
    window.clipboard_clear()
    window.clipboard_append(short_url.get())

window = tk.Tk()
window.geometry("400x300")
window.title('Short Link v0.1')

lbl = tk.Label(window, text="Сокращение ссылок", font=("Arial Bold", 29))
lbl.grid(column=0, row = 0)

lbl1 = tk.Label(window, text="Введите ссылку для сокращения ниже")
lbl1.grid(column=0, row=1)

url = tk.Entry(window, width=45)
url.grid(column=0, row=2)

btn_short = tk.Button(window, text="Сократить ссылку", command=clicked)
btn_short.grid(column=0, row=3)

lbl2 = tk.Label(window, text='Сокращенная ссылка будет ниже')
lbl2.grid(column=0, row=4)

short_url = tk.Entry(window, width=45)
short_url.grid(column=0, row=5)

btn_copy = tk.Button(window, text="Скопировать готовую ссылку", command=copy_link)
btn_copy.grid(column=0, row=6)

window.mainloop()
