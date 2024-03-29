import tkinter
import customtkinter
import basic_operations
import differentiation_integration
import function_value
import newtons_method
import input_output
from functools import partial

# tabe ha. har kodam as input_output tabe haye amade konande voroodi
# va khorooji ra seda mikonand
def call_integrate(): # special function to parse c
    a = input_output.ready_input(str(inp1.get()))
    result = differentiation_integration.integrate(a, int(inp2.get()))
    result = input_output.ready_output(result)
    input_output.output(result)

def call_derivative():
    a = input_output.ready_input(str(inp1.get()))
    result = differentiation_integration.differentiate(a, int(inp2.get()))
    result = input_output.ready_output(result)
    input_output.output(result)

def call_evaluate():
    a = input_output.ready_input(str(inp1.get()))
    result = function_value.evaluate(a, int(inp2.get()))
    input_output.output(result)

def call_root():
    a = input_output.ready_input(str(inp1.get()))
    result = newtons_method.find_root(a)
    input_output.output(result)

def call_add():
    a = input_output.ready_input(str(inp1.get()))
    b = input_output.ready_input(str(inp2.get()))
    result = basic_operations.add(a, b)
    result = input_output.ready_output(result)
    input_output.output(result)

def call_subtract():
    a = input_output.ready_input(str(inp1.get()))
    b = input_output.ready_input(str(inp2.get()))
    result = basic_operations.subtract(a, b)
    result = input_output.ready_output(result)
    input_output.output(result)

def call_multiply():
    a = input_output.ready_input(str(inp1.get()))
    b = input_output.ready_input(str(inp2.get()))
    result = basic_operations.multiply(a, b)
    result = input_output.ready_output(result)
    input_output.output(result)

def call_divide(): #quotient and remainder
    a = input_output.ready_input(str(inp1.get()))
    b = input_output.ready_input(str(inp2.get()))
    result = basic_operations.divide(a, b)
    result = input_output.ready_output(result[0])
    input_output.output(result)

# settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# initialization
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Polynomial calculator')

# input
inp1 = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=inp1)
entry.pack()

inp2 = tkinter.StringVar()
entry2 = customtkinter.CTkEntry(app, width=350, height=40, textvariable=inp2)
entry2.pack()

# buttons
calculate = customtkinter.CTkButton(app, text='Integral', command=call_integrate)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='derivative', command=call_derivative)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='evaluate', command=call_evaluate)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='root', command=call_root)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='add', command=call_add)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='subtract', command=call_subtract)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='multiply', command=call_multiply)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='divide', command=call_divide)
calculate.pack()


# ejraye GUI
app.mainloop()