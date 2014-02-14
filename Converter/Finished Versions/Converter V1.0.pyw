#Imports
from tkinter import *
from tkinter import ttk

#Initiates the GUI
root = Tk()
root.title("Converter")

#Creates the frame to hold everything
mainframe = ttk.Frame(root, borderwidth=5, relief="flat", width=50, height=50, padding = "10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#String variables for labels and inputs/ outputs
NumberToConvert = StringVar()
Output = StringVar()

#Function to convert something to binary
#Coded by Liam
def ConvertToBinary():
    array = []
    x = int(InputBox.get())
    i = 2
    j = 0
  
    while i <= x:
        i = i * 2

    i = i / 2
    while i > 1:
        
        if x >= i:
            array.append(1)
            x = x - i
        else:
            array.append(0)
        i = i / 2

    array.append(int(x))
    s = ""
    while j < len(array):
        z = array[j]    
        s = str(s) + str(z)
        j = j + 1

    Output.set(s)

#Function to convert to decimal
#Coded by Liam
def ConvertToDecimal():
    array = []
    x = int(InputBox.get())
    i = 1
    j = 0

    while i <= x:
        i = i * 10

    i = i / 10
    while i > 1:
        c = x / i
        if x >= i:
            x = x - i
        array.append(int(c))
        i = i / 10
        
    array.append(int(x))

    j = len(array) - 1
    a = 1
    while j > 0:
        a = a * 2
        j = j - 1

    s = 0
    b = 0
    while b < len(array):
        z = a * array[b]
        a = a / 2
        b = b + 1
        s = s + z
        
    Output.set(int(s))


#Creates the labels, buttons and input    
InfoLabel = ttk.Label(mainframe, text='Input number to convert then click appropriate button')
OutputLabel = ttk.Label(mainframe, textvariable = Output)
BinaryButton= ttk.Button(mainframe, text = 'Convert to Binary', command = ConvertToBinary)
DecimalButton = ttk.Button(mainframe, text = 'Convert to Decimal', command = ConvertToDecimal)
InputBox = ttk.Entry(mainframe, textvariable=NumberToConvert)

#Aligns the widgets to a grid
InfoLabel.grid(column=1, row=1, columnspan=2)
InputBox.grid(column=1, row=2, columnspan=3)
OutputLabel.grid(column=3, row=2)
BinaryButton.grid(column=1, row=3)
DecimalButton.grid(column=2, row=3)

#Sets the output to 0, ready for the first sum
Output.set(0)

#Something to do with the grid. Not 100% sure what it does, but seems needed
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

#Starts the program
root.mainloop();
