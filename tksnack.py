from Tkinter import *
import tkMessageBox

class App(object):
    snack = ""
    
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Synack")
        self.label = Label (self.root, text= "What snack?")
        self.label.pack()


        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Calculate")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()


    def clicked1(self):
        self.snack = self.entrytext.get()
        #result = int(input)*2
        #self.label.configure(text=result)

    def button_click(self, e):
        pass

if __name__ == '__main__':
    app = App()
    print app.snack
