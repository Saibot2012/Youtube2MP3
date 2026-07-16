import customtkinter as ctk
from gui import App

ctk.set_appearance_mode("System") #Light, Dark or default
ctk.set_default_color_theme("blue")

app = App()
app.mainloop()