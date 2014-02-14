#imports
from tkinter import *
from tkinter import ttk

#Initiates the GUI
root = Tk()
root.title("Temperature Converter")
root.resizable(FALSE,FALSE)

#Creates the frames to hold everything
mainframe = ttk.Frame(root, borderwidth=5, relief="flat", width=200, height=100, padding = "10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)

#string vars
Output = StringVar()
Input = StringVar()
FirstDropdownString = StringVar()
SecondDropdownString = StringVar()

#functions
def Convert():
    global FirstDropdownString
    global SecondDropdownString
    global Input
    global Output
    if Input.get().strip() != '':
        if FirstDropdownString.get() == 'Celcius':
            if int(Input.get()) >= -273:
                if SecondDropdownString.get() == 'Celcius':
                    Output.set('Same scale!') 
                elif SecondDropdownString.get() == 'Fahrenheit':
                    TempInt = int(Input.get())
                    TempInt = (9/5)*TempInt+32
                    TempInt = int(TempInt)
                    TempStr = str(TempInt)
                    Output.set(TempStr)
                elif SecondDropdownString.get() == 'Kelvin':
                    TempInt = int(Input.get()) + 273
                    TempStr = str(TempInt)
                    Output.set(TempStr)
            else:
                Output.set('Too Cold! Brr!')
        elif FirstDropdownString.get() == 'Fahrenheit':
            if int(Input.get()) >= -460:
                if SecondDropdownString.get() == 'Celcius':
                    TempInt = int(Input.get())
                    TempInt = (5/9)*(TempInt-32)
                    TempInt = int(TempInt)
                    TempStr = str(TempInt)
                    Output.set(TempStr)
                elif SecondDropdownString.get() == 'Fahrenheit':
                    Output.set('Same scale!') 
                elif SecondDropdownString.get() == 'Kelvin':
                    TempInt = int(Input.get())
                    TempInt = (5/9)*(TempInt-32)
                    TempInt = int(TempInt)
                    TempInt = TempInt + 273
                    TempStr = str(TempInt)
                    Output.set(TempStr)
            else:
                Output.set('Too Cold! Brr!')
        elif FirstDropdownString.get() == 'Kelvin':
            if int(Input.get()) >= 0:
                if SecondDropdownString.get() == 'Celcius':
                    TempInt = int(Input.get()) - 273
                    TempStr = str(TempInt)
                    Output.set(TempStr)
                elif SecondDropdownString.get() == 'Fahrenheit':
                    TempInt = int(Input.get()) - 273
                    TempInt = (9/5)*TempInt+32
                    TempInt = int(TempInt)
                    TempStr = str(TempInt)
                    Output.set(TempStr)
                elif SecondDropdownString.get() == 'Kelvin':
                    Output.set('Same scale!') 
            else:
                Output.set('Too Cold! Brr!')
    else:
        Output.set('No Input')

def Swap():
    FirstDropdownString.set(SecondDropdownString.get())
    SecondDropdownString.set(TempStr)
    
#Widgets
InputBox = ttk.Entry(mainframe, textvariable=Input)
ConvertButton = ttk.Button(mainframe, command=Convert, text='Convert')
FirstDropdown = ttk.Combobox(mainframe, textvariable=FirstDropdownString)
SwapButton = ttk.Button(mainframe, command=Swap, text='↔')
SecondDropdown = ttk.Combobox(mainframe, textvariable=SecondDropdownString)
EqualsLabel = ttk.Label(mainframe, text='=')
CreditsLabel = ttk.Label(mainframe, text='Made by David')
OutputLabel = ttk.Label(mainframe, textvariable=Output)

#grid
InputBox.grid(column=1, row=1, columnspan=1, sticky='N E W S')
EqualsLabel.grid(column=2, row=1, columnspan=1, sticky='N S')
OutputLabel.grid(column=3, row=1, columnspan=1, sticky='N S')
ConvertButton.grid(column=4, row=1, columnspan=1, sticky='N E W S')
FirstDropdown.grid(column=1, row=2, columnspan=1, sticky='N E W S')
SwapButton.grid(column=2, row=2, columnspan=1, sticky='N E W S')
SecondDropdown.grid(column=3, row=2, columnspan=1, sticky='N E W S')
CreditsLabel.grid(column=4, row=2, sticky='N S W E')

#Dropdown options
FirstDropdown['state'] = ('readonly')
SecondDropdown['state'] = ('readonly')
FirstDropdown['values'] = ('Celcius', 'Fahrenheit', 'Kelvin')
FirstDropdown.set('Celcius')
SecondDropdown['values'] = ('Celcius', 'Fahrenheit', 'Kelvin')
SecondDropdown.set('Fahrenheit')

#Sets the output to null
Output.set('No Input')

#Adds padding to the grid
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

#Starts the program
root.mainloop();
