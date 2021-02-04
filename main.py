import tkinter as tk
import pyshorteners as ps
import json


def short_link(user_link):
    """Get short link"""
    link = ps.Shortener()
    short_link = link.tinyurl.short(user_link)
    return short_link


def langue():
    with open("langue.json", "r") as read_file:
        langs = json.load(read_file)
    for lang in langs:
        if lang["langue"] == 'english':
            return lang


def clicked():
    """Main button to create short link, change state to normal"""
    link = url.get()
    ready_link = short_link(link)
    short_url.configure(state='normal')
    short_url.insert(0, ready_link)


def copy():
    """Button to copy ready short link in clipboard"""
    window.clipboard_clear()
    window.clipboard_append(short_url.get())


"""Main settings window"""
window = tk.Tk()
window.geometry("370x300")
window.title('Short Link v0.1')
window.resizable(width=False, height=False)
lang = langue()

"""Main label aplication"""
lbl = tk.Label(window, text=lang['label1'], font=("Arial Bold", 31))
lbl.grid(column=0, row=0)

"""Text for first text to enter text"""
lbl1 = tk.Label(window, text=lang['label2'])
lbl1.grid(column=0, row=1)

"""Window to write link and focus in window"""
url = tk.Entry(window, width=45)
url.focus()
url.grid(column=0, row=2)

"""Button to create short link"""
btn_short = tk.Button(window, text=lang['button1'], command=clicked)
btn_short.grid(column=0, row=3)

"""Label to copy short link"""
lbl2 = tk.Label(window, text=lang['label3'])
lbl2.grid(column=0, row=4)

"""Window to copy link, begin disabled"""
short_url = tk.Entry(window, width=45, state='disabled')
short_url.grid(column=0, row=5)

"""Window to auto copy link in clipboard"""
btn_copy = tk.Button(window, text=lang['button2'], command=copy)
btn_copy.grid(column=0, row=6)

"""Main loop aplication"""
window.mainloop()
