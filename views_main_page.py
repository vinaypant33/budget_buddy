import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as tbs

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class Main_Page():
    
    # Function : when any configure
    def configure_data(self , event):
        self.adjusted_height = self.main_page.winfo_height()
        self.adjusted_width = self.main_page.winfo_width() - self.sidebar_frame.winfo_width()
        self.scrollbar_frame.configure(height = self.adjusted_height , width = self.adjusted_width)


    def __init__(self) -> None:
        self.main_page  = ctk.CTk()
        self.main_page.title("Budget Buddy")
        # check the center of the screen and the width and the height of the app  : 
        self.screen_height  = self.main_page.winfo_screenheight()
        self.screen_width  =  self.main_page.winfo_screenwidth()
        self.y_location  = self.screen_height // 2 - 300 # FOr now have done the hard coding in here will change the height and the width with dynamic code later 
        self.x_location  = self.screen_width // 2 - 450
        self.main_page.geometry(f"900x600+{self.x_location}+{self.y_location}")

        # Will change the icon of the app here with the custom image icon for app : 

        # Defining the controls  : 
        # Frame : It will load all the app subframes and will be shown as the tab bar : sidebar to be added in the app  : 
        self.scrollbar_frame  = ctk.CTkScrollableFrame(self.main_page , height=600 , width=900)
        self.sidebar_frame = tk.Frame(self.main_page , height=900 , width=60)
        # placing the controls : 
        self.sidebar_frame.pack(side="left" , fill="both")
        self.main_page.bind("<Configure>" , self.configure_data)
        self.scrollbar_frame.pack(fill="y")
    # Running the main app  : 
        self.main_page.mainloop()



if __name__ == '__main__':
    main = Main_Page()
    


