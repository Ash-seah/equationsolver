import tkinter
import customtkinter

# settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# initialization
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Polynomial calculator')

# input
inp = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=inp)
entry.pack()

# ejraye GUI
app.mainloop()