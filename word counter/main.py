from tkinter import *
from tkinter import messagebox


# ---------------------------- counter ------------------------------- #
def counter():
    words = text_entry.get()
    w, c = 0, 0
    for i in words:
        print(i)
        c += 1
    for i in words.split():
        print(i)
        w += 1
    messagebox.showinfo(title="Total Words", message=f"There are {w} word/s and {c} character/s")


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.config(padx=50, pady=50)
root.minsize(300, 300)
root.title("Word Counter")
root.eval('tk::PlaceWindow . center')


# label
text = Label(text="Paste to Count")
text.grid(column=0, row=1)

# entry
text_entry = Entry(width=35)
text_entry.grid(column=0, row=2, columnspan=1)
text_entry.focus()

# button
button = Button(text="Count", command=counter)
button.grid(column=0, row=3)

root.mainloop()
