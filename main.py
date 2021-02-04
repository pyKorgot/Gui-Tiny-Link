import tkinter as tk
import pyshorteners as ps


def short_link(user_link):
    """Get short link"""
    link = ps.Shortener()
    short_link = link.tinyurl.short(user_link)
    return short_link


def clicked():
    """Main button to create short link"""
    link = url.get()
    ready_link = short_link(link)
    short_url.insert(0, ready_link)


def copy():
    """Button to copy ready short link in clipboard"""
    window.clipboard_clear()
    window.clipboard_append(short_url.get())


"""Main settings window"""
window = tk.Tk()
window.geometry("400x300")
window.title('Short Link v0.1')

"""Main label aplication"""
lbl = tk.Label(window, text="Сокращение ссылок", font=("Arial Bold", 29))
lbl.grid(column=0, row=0)

"""Text for first text to enter text"""
lbl1 = tk.Label(window, text="Введите ссылку для сокращения ниже")
lbl1.grid(column=0, row=1)

"""Window to write link"""
url = tk.Entry(window, width=45)
url.grid(column=0, row=2)

"""Button to create short link"""
btn_short = tk.Button(window, text="Сократить ссылку", command=clicked)
btn_short.grid(column=0, row=3)

"""Label to copy short link"""
lbl2 = tk.Label(window, text='Сокращенная ссылка будет ниже')
lbl2.grid(column=0, row=4)

"""Window to copy link"""
short_url = tk.Entry(window, width=45)
short_url.grid(column=0, row=5)

"""Window to auto copy link in clipboard"""
btn_copy = tk.Button(window, text="Скопировать готовую ссылку", command=copy)
btn_copy.grid(column=0, row=6)

"""Main loop aplication"""
window.mainloop()
