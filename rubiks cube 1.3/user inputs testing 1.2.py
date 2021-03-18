from tkinter import *

class TKinter_screen(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x400')
        self.title('rubiks cube solver input screen')

        self.options = ['White','Green','Orange','Blue','Red','Yellow']
        self.option_var = [
            [StringVar(self),StringVar(self),StringVar(self)],
            [StringVar(self),StringVar(self),StringVar(self)],
            [StringVar(self),StringVar(self),StringVar(self)]
        ]

        self.create_options()

    def create_options(self):
        _1 = OptionMenu(self, self.option_var[0][0], *self.options).grid(row=3, column=4)
        _2 = OptionMenu(self, self.option_var[0][1], *self.options).grid(row=3, column=5)
        _3 = OptionMenu(self, self.option_var[0][2], *self.options).grid(row=3, column=6)
        _4 = OptionMenu(self, self.option_var[1][0], *self.options).grid(row=4, column=4)
        _5 = OptionMenu(self, self.option_var[1][2], *self.options).grid(row=4, column=6)
        _6 = OptionMenu(self, self.option_var[2][0], *self.options).grid(row=5, column=4)
        _7 = OptionMenu(self, self.option_var[2][1], *self.options).grid(row=5, column=5)
        _8 = OptionMenu(self, self.option_var[2][2], *self.options).grid(row=5, column=6)

# options_dict = {'White' : W, 'Green': G,'Orange': O,'Blue': B,'Red': R,'Yellow': Y}



if __name__ == "__main__":
    root = TKinter_screen()
    root.attributes('-alpha', 0.5)
    root.mainloop()