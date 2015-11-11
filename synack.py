# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 13:16:14 2015
SUPER AUTOMATED SNACKAHACK
@author: keith
"""


from Tkinter import *
import csv

class App:

    ## Attributes to be processed after GUI finishes
    snack = None
    count = 0
    seller = None
    
    perm_snack = None
    perm_seller = None
    perm_count = None
    perm_price = None
    
    
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        self.snacks = []
        pics = []
        self.prices = []
        with open('GUI.conf', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.snacks.append(row[0])
                pics.append(row[1])
                self.prices.append(int(row[2]))
        
        
        self.top_label = Label(master, text="What snack?")
        self.top_label.pack()

        #print snacks        
        
        self.snack = StringVar(master)
        self.snack.set("NOT SELECTED")
                
        self.option_menu = apply(OptionMenu, (master, self.snack) + tuple(self.snacks))#OptionMenu(master, self.snack, snacks[0], snacks[1], snacks[2])
        self.option_menu.pack()
        
        self.top_label = Label(master, text="Who sold it?")
        self.top_label.pack()

        
        sellers = ["Keith", "Jon", "Jose"]        
        self.seller = StringVar(master)       
        self.seller.set("NOT SELECTED")

        self.seller_menu = apply(OptionMenu, (master, self.seller) + tuple(sellers))        
        self.seller_menu.pack()
        
        self.top_label = Label(master, text="How many?")
        self.top_label.pack()        
        
        self.entrytext = StringVar()
        Entry(master, textvariable=self.entrytext).pack()        
        
        self.buttontext = StringVar()
        self.buttontext.set("Confirm Order")
        Button(master, textvariable=self.buttontext, command=self.clicked).pack()        
        
    
        '''
        self.quit_button = Button(frame, text="QUIT", 
                                  fg="red", command=frame.quit)
        self.quit_button.pack(side=LEFT)
        '''
    def clicked(self):
        self.perm_seller = self.seller.get()
        self.perm_snack = self.snack.get()
        self.perm_count = int(self.entrytext.get())  
        index = self.snacks.index(self.perm_snack)
        self.perm_price = self.perm_count * self.prices[index]
        string = "Price = $" + str(self.perm_price)      
        label = Label(Toplevel(), text=string, height=0, width=20)        
        label.pack()        
        
if __name__ == '__main__':
    root = Tk()
    root.wm_title("Snack-Hack")
    
    
    app = App(root)
    
    root.mainloop()
    print app.perm_seller    
    print app.perm_snack
    print app.count
    #root.destroy()