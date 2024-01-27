import tkinter
import customtkinter
import basic_operations
import differentiation_integration
import function_value
import newtons_method
import input_output
from functools import partial

def call(func):
    a = input_output.ready_input(str(inp1.get()))

    if func == 'integral':
        b = int(inp2.get())
        print(differentiation_integration.integrate(a, int(b))) #fix
    elif func == 'derivative':
        result = differentiation_integration.differentiate(a, int(inp2.get()))
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'evaluate':
        result = function_value.evaluate(a, int(inp2.get()))
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'root':
        result = newtons_method.find_root(a, int(inp2.get()))
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'add':
        b = input_output.ready_input(str(inp2.get()))
        result = basic_operations.add(a, b)
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'subtract':
        b = input_output.ready_input(str(inp2.get()))
        result = basic_operations.subtract(a, b)
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'multiply':
        b = input_output.ready_input(str(inp2.get()))
        result = basic_operations.multiply(a, b)
        result = input_output.ready_output(result)
        input_output.output(result)
    elif func == 'divide':
        b = input_output.ready_input(str(inp2.get()))
        result = basic_operations.divide(a, b)
        result = input_output.ready_output(result)
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
calculate = customtkinter.CTkButton(app, text='Integral', command=lambda: call('integrate'))
calculate.pack()

calculate = customtkinter.CTkButton(app, text='derivative', command=lambda: call('derivative'))
calculate.pack()

calculate = customtkinter.CTkButton(app, text='evaluate', command=call)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='root', command=call)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='add', command=call)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='subtract', command=call)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='multiply', command=call)
calculate.pack()

calculate = customtkinter.CTkButton(app, text='divide', command=call)
calculate.pack()


# ejraye GUI
app.mainloop()