import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as tbs



class Main_Page():

    def __init__(self) -> None:
        self.main_page  = ctk.CTk()
        self.main_page.title("Budget Buddy")




    # Running the main app  : 
        self.main_page.mainloop()



if __name__ == '__main__':
    main = Main_Page()
    


