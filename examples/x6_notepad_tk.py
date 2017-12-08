from tkinter import (Tk, Text, Menu,
                     messagebox, filedialog, END)

class Notepad(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._text_edit = Text(self)
        self._text_edit.pack()

        menu_bar = Menu(self)
        self['menu'] = menu_bar
        menu_file = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=menu_file)
        menu_file.add_command(label='Open', command=self.open)
        menu_file.add_command(label='Save', command=self.save)
        menu_file.add_command(label='Quit', command=self.quit)

    def quit(self):
        if messagebox.askokcancel('Quit', 'Are you sure?'):
            self.destroy()

    def open(self):
        fn = filedialog.askopenfilename()
        if fn:
            with open(fn, mode='r') as f:
                contents = f.read()
                self._text_edit.delete(1.0, END)
                self._text_edit.insert(END, contents)

    def save(self):
        fn = filedialog.asksaveasfilename()
        if fn:
            with open(fn, mode='w') as f:
                contents = self._text_edit.get(1.0, END)
                f.write(contents)

if __name__ == '__main__':
    win = Notepad()
    win.mainloop()
