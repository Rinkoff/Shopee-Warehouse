from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from core.const import *


class MainPage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        #Put in main frame background
        self.config(background="#ebe5e4")

        #Generate frame for settings option
        self.menu = tk.Frame(self,bg="#e8e2e1")
        menu_height = WINDOW_HEIGHT - 120
        self.menu.place(y = 120,width=300,height=menu_height)

        #Generating frame for user data(PIC and Warehouse name)
        self.user_data = tk.Frame(self,bg="#e8e2e1")
        self.user_data.place(width=300, height=120)
        bottom_line = tk.Frame(self.user_data, height=1, width=200, bg="#cfcdcc")
        bottom_line.pack(side="bottom", fill="x")

        #Put default image
        market_img = Image.open("assets/images/google-cloud-marketplace.png").resize((75, 75))
        self.tk_market_img = ImageTk.PhotoImage(market_img)
        self.market_logo = ttk.Label(self.user_data,image=self.tk_market_img)
        self.market_logo.place(rely=0.15, relx=0.07)

        #Put Marketplace name
        self.market_name = ttk.Label(self.user_data, text= "My Personal Store",font=('Arial', 16), background="#e8e2e1")
        label_width = self.market_name.winfo_reqwidth()
        label_height = self.market_name.winfo_reqheight()
        x_value = (200 - label_width) / 2 + 100
        y_value = (120 - label_height) / 2
        self.market_name.place(x = x_value,y=y_value)

        #Generate menu options
        self.labels = {}

        for option in SETTINGS_OPTIONS:
            label = ttk.Label(self.menu, text=option,font=("Ariel",16),background="#e8e2e1")
            label.pack(anchor="w",pady=20)
            self.labels[option] = label


        #Make a search bar
        self.searchbar = ttk.Entry(self,font = 20,validate="key",foreground="#b8b8b8")
        self.searchbar.place(relx= 0.38,rely=0.04,relwidth=0.6,relheight=0.07)
        self.searchbar.insert(0, "Search...")
        self.searchbar.bind("<FocusIn>", self.on_entry_click)
        self.searchbar.bind("<FocusOut>", self.on_entry_focusout)
        # self.searchbar.bind("<<Modified>>", self.on_modified_search())

        #Make a listbox with items
        self.product_tw = ttk.Treeview(self)
        self.product_tw.place(relx= 0.29,rely=0.2,relwidth=0.689, relheight=0.75)

        self.product_tw["columns"] = SECTIONS
        self.product_tw.heading("#0", text="", anchor=tk.W)
        self.product_tw.column("#0",width=0)
        for section in SECTIONS:
            self.product_tw.heading(section, text=section)
            self.product_tw.column(section, width=40)

        print(self.labels)

        # Add Section Label effects
        self.labels["Add Section"].bind("<Button-1>", self.add_section_click)
        self.labels["Add Section"].bind("<Enter>",lambda event: self.label_hover(event,self.labels["Add Section"]))
        self.labels["Add Section"].bind("<Leave>", lambda event: self.label_hover_off(event, self.labels["Add Section"]))

        #Remove Section Label effects
        self.labels["Remove Section"].bind("<Button-1>", self.remove_section_click)
        self.labels["Remove Section"].bind("<Enter>", lambda event: self.label_hover(event, self.labels["Remove Section"]))
        self.labels["Remove Section"].bind("<Leave>",
                                        lambda event: self.label_hover_off(event, self.labels["Remove Section"]))

        #Add Status Label effects
        self.labels["Add Status"].bind("<Button-1>", self.add_status_click)
        self.labels["Add Status"].bind("<Enter>", lambda event: self.label_hover(event, self.labels["Add Status"]))
        self.labels["Add Status"].bind("<Leave>",
                                        lambda event: self.label_hover_off(event, self.labels["Add Status"]))

        #New Warehouse Label effects
        self.labels["New Warehouse"].bind("<Button-1>", self.new_warehouse_click)
        self.labels["New Warehouse"].bind("<Enter>", lambda event: self.label_hover(event, self.labels["New Warehouse"]))
        self.labels["New Warehouse"].bind("<Leave>",
                                        lambda event: self.label_hover_off(event, self.labels["New Warehouse"]))

        #Switch Warehouses Label effects
        self.labels["Switch Warehouses"].bind("<Button-1>", self.switch_warehouse_click)
        self.labels["Switch Warehouses"].bind("<Enter>", lambda event: self.label_hover(event, self.labels["Switch Warehouses"]))
        self.labels["Switch Warehouses"].bind("<Leave>",
                                        lambda event: self.label_hover_off(event, self.labels["Switch Warehouses"]))

    def on_entry_click(self, event):
        if self.searchbar.get() == "Search...":
            self.searchbar.delete(0, "end")
            self.searchbar.insert(0, "")
            self.searchbar.config(foreground="#080808")

    def on_entry_focusout(self,event):
        if self.searchbar.get() == "":
            self.searchbar.insert(0, "Search...")
            self.searchbar.config(foreground="#b8b8b8")

    # def on_modified_search(self,event):
    #     if self.searchbar.edit_modified():
    #         self.search()
    #     self.searchbar.edit_modified(False)

    def add_section_click(self,event):
        pass

    def remove_section_click(self,event):
        pass

    def add_status_click(self,event):
        pass

    def new_warehouse_click(self,event):
        pass

    def switch_warehouse_click(self,event):
        pass
    def label_hover(self,event,label):
        label.config(foreground="#ababab")

    def label_hover_off(self,event,label):
        label.config(foreground="#000000")
