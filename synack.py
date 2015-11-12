# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 13:16:14 2015
SUPER AUTOMATED SNACKAHACK
@author: keith
"""


from Tkinter import *
import csv
import yaml

class App:

    ## Configuration YAML file -  default name to search for is config.yaml
    ## Default name in App.__init__ keyword
    yaml_filename = None
    yaml_dict = None
    
    ## CSV where data will be written into
    csv_filename = None

    ## Lists to be read from the YAML configuration file
    sellers = []
    items = []

    ## Attributes to be processed after GUI finishes
    snack = None
    count = 0
    seller = None
    
    def __init__(self, master, yaml_filename="config.yaml"):
        
        # Sets the YAML filename to keyword argument
        self.yaml_filename = yaml_filename

        # Creates the frame with parameters
        frame = Frame(master)
        frame.pack()
        
        self._loadconfigfile() 
        
        self.top_label = Label(master, text="What snack?")
        self.top_label.pack()

        #print snacks        
        
        self.snack = StringVar(master)
        self.snack.set("NOT SELECTED")
                
        self.option_menu = apply(OptionMenu, (master, self.snack) + tuple(self.items))
        self.option_menu.pack()
        
        self.top_label = Label(master, text="Who sold it?")
        self.top_label.pack()

        
        self.seller = StringVar(master)       
        self.seller.set("NOT SELECTED")

        self.seller_menu = apply(OptionMenu, (master, self.seller) + tuple(self.sellers))        
        self.seller_menu.pack()
        
        self.top_label = Label(master, text="How many?")
        self.top_label.pack()        
        
        self.entrytext = StringVar()
        Entry(master, textvariable=self.entrytext).pack()        
        
        self.buttontext = StringVar()
        self.buttontext.set("Confirm Order")
        Button(master, textvariable=self.buttontext, command=self.clicked).pack()        
        
    def _loadconfigfile(self):
        with open(self.yaml_filename, 'r') as f:
            self.yaml_dict = yaml.load(f) 

        self.sellers = self.yaml_dict["sellers"]
        self.items = map(lambda x: x["name"], self.yaml_dict["items"])

    
    def clicked(self):
        seller = self.seller.get()
        snack = self.snack.get()
        self.count = int(self.entrytext.get())  
        price = self.count 
        print "price"
        for x in self.yaml_dict["items"]:
            if x["name"] == snack: price *= x["price"]
        string = "Price = $" + str(price)      
        label = Label(Toplevel(), text=string, height=0, width=20)        
        label.pack()        
        
if __name__ == '__main__':
    root = Tk()
    root.wm_title("Snack-Hack")
    
    
    app = App(root)
    
    root.mainloop()
    print app.seller    
    print app.snack
    print app.count
