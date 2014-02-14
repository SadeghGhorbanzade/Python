#Imports
from tkinter import *
from tkinter import ttk

#Initiates the GUI
root = Tk()
root.title("Converter")

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

#String variables for labels and inputs/ outputs
NumberToConvert = StringVar()
SecondNumberToConvert = StringVar()
MathsOperator = StringVar()
Converter = StringVar()
Output = StringVar()
OutputType = StringVar()

#Function to convert to decimal
#Coded by Liam
def ConvertBinToDecimal(Input):
    number = Input
    base = pow(2, len(number))
    string = 0
    for decon in number:
        if 1 < int(decon) or int(decon) < 0:
            string = 'Invalid Input'
            break
        base = base / 2
        string = string + (base * int(decon))
    return(string)

def DecimalToBinary(Input):
    number = int(Input)
    base = 2
    string = ""

    while base <= number:
        base = base * 2
    while base > 1:
        base = base / 2
        if number >= base:
            dataval = 1
            number = number - base
        else:
            dataval = 0
        string = string + str(dataval)
    return(string)

def BinaryToHex(Input):
    number = Input
    #asks for a number input from the user
    output = ""
    section = ""
    #prepares an output and section string
    runs = 0
    antinegative = 0
    #prepares two counting variables
    hexi = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    #a directory / dictionary that holds the preset values for binary to hexidecimal
    while antinegative < len(number):
        antinegative = antinegative + 4
    #makes it so the line below will not return a negative value
    failsafe = antinegative - len(number)
    #adds a failsafe which prevents there being a fault because the length of the
    #string may not be equal to 4
    while failsafe > 3:
        failsafe = failsafe - 4
    #finds how many 0's need to be added on to number
    while failsafe > 0:
        number = '0' + number
        failsafe = failsafe - 1
    #adds the required amount
    for retreving in number:
        section = section + retreving
        runs = runs + 1
    #creates a variable that will be 4 characters long for referance to the directory
        if runs == 4:
            runs = 0
            output = output + hexi[section]
            section = ""
    #makes it so the section and runs are reset for the next run through of the loop
    #creates the output by inputting the section variable to corresond to the correct
    #hexidecimal value        
    return(output)

def HexToBinary(Input):
    number = Input
    number = number.upper()
    #Ask for a number in Hex
    output = ""
    #defines output outside of the loop
    hexi = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    #a directory / dictionary of the preset values for each of the individual hexidecimal values to binary
    for retreving in number:
        if retreving > 'F':
            output = 'Invalid Input'
            break
        else:
    #takes all of the individual characters out of the number string and assigns them to retrieving one at a time
            output = output + hexi[retreving]
    #inputs the characters from the string and add them to a variable after canverting them using the directory
    return(output)

def Compute():
    if Converter.get() == 'Convert Decimal to Binary' and InputBox.get().isdigit():
        Output.set(DecimalToBinary(int(InputBox.get())))
        OutputType.set('Binary')
        
    elif Converter.get() == 'Convert Decimal to Hexadecimal' and InputBox.get().isdigit():
        TempVar = DecimalToBinary(int(InputBox.get()))
        Output.set(BinaryToHex(str(TempVar)))
        OutputType.set('Hexadecimal')
        
    elif Converter.get() == ('Convert Binary to Decimal') and InputBox.get().isdigit():
        Output.set(ConvertBinToDecimal(InputBox.get()))
        OutputType.set('Decimal')
        
    elif Converter.get() == ('Convert Binary to Hexadecimal') and InputBox.get().isdigit():
        Output.set(BinaryToHex(str(InputBox.get())))
        OutputType.set('Hexadecimal')
        
    elif Converter.get() == ('Convert Hexadecimal to Decimal') and InputBox.get().isalnum():
        TempVar = HexToBinary(InputBox.get())
        Output.set(ConvertBinToDecimal(TempVar))
        OutputType.set('Decimal')
        
    elif Converter.get() == ('Convert Hexadecimal to Binary') and InputBox.get().isalnum():
        Output.set(HexToBinary(InputBox.get()))
        OutputType.set('Binary')
        
    elif Converter.get() == 'Binary Mathematics' and InputBox.get().isdigit() and SecondInputBox.get().isdigit():
        print('Step 1')
        FirstNumber = ConvertBinToDecimal(InputBox.get())
        SecondNumber = ConvertBinToDecimal(SecondInputBox.get())
        FirstNumber = str(int(FirstNumber))
        SecondNumber = str(int(SecondNumber))
        print(FirstNumber)
        print(SecondNumber)
        OutputType.set('Binary')
        if FirstNumber.isdigit() and SecondNumber.isdigit():
            print('Step 2')
            if MathsOperatorDropdown.get() == '+':
                Output.set(DecimalToBinary(str(int(FirstNumber)+int(SecondNumber))))
                
            elif MathsOperatorDropdown.get() == '-':
                print('-')
                Output.set(DecimalToBinary(str(int(FirstNumber)-int(SecondNumber))))
                
            elif MathsOperatorDropdown.get() == 'x':
                print('x')
                Output.set(DecimalToBinary(str(int(FirstNumber)*int(SecondNumber))))
                
            elif MathsOperatorDropdown.get() == '/':
                print('/')
                Output.set(DecimalToBinary(str(int(int(FirstNumber)/int(SecondNumber)))))
        else:
            Output.set('Invalid Input')
            
    elif Converter.get() == 'Hexadecimal Mathematics' and InputBox.get().isalnum() and SecondInputBox.get().isalnum():
        FirstNumber = HexToBinary(InputBox.get())
        SecondNumber = HexToBinary(SecondInputBox.get())
        OutputType.set('Hexadecimal')
        if FirstNumber.isdigit() and SecondNumber.isdigit():
            FirstNumber = str(int(ConvertBinToDecimal(FirstNumber)))
            SecondNumber = str(int(ConvertBinToDecimal(SecondNumber)))
            if FirstNumber.isdigit() and SecondNumber.isdigit():
                if MathsOperatorDropdown.get() == '+':
                    FirstNumber = int(FirstNumber)
                    SecondNumber = int(SecondNumber)
                    InputNumber = str(FirstNumber+SecondNumber)
                    InputNumber = DecimalToBinary(InputNumber)
                    InputNumber = BinaryToHex(InputNumber)
                    Output.set(InputNumber)
                    
                elif MathsOperatorDropdown.get() == '-':
                    FirstNumber = int(FirstNumber)
                    SecondNumber = int(SecondNumber)
                    InputNumber = str(FirstNumber-SecondNumber)
                    InputNumber = DecimalToBinary(InputNumber)
                    InputNumber = BinaryToHex(InputNumber)
                    Output.set(InputNumber)
                    
                elif MathsOperatorDropdown.get() == 'x':
                    FirstNumber = int(FirstNumber)
                    SecondNumber = int(SecondNumber)
                    InputNumber = str(FirstNumber*SecondNumber)
                    InputNumber = DecimalToBinary(InputNumber)
                    InputNumber = BinaryToHex(InputNumber)
                    Output.set(InputNumber)
                    
                elif MathsOperatorDropdown.get() == '/':
                    FirstNumber = int(FirstNumber)
                    SecondNumber = int(SecondNumber)
                    InputNumber = str(FirstNumber/SecondNumber)
                    InputNumber = DecimalToBinary(InputNumber)
                    InputNumber = BinaryToHex(InputNumber)
                    Output.set(InputNumber)
            else:
                Output.set('Invalid Input')
        else:
            Output.set('Invalid Input')
    else:
        Output.set('Invalid Input')
        
def ConverterDropdownChanged(*args): 
    if Converter.get() == 'Binary Mathematics' or Converter.get() == 'Hexadecimal Mathematics':
        TurnOnOperators()
    else:
        TurnOffOperators()
    
def TurnOnOperators():
    MathsOperatorDropdown['state'] = ('readonly')
    SecondInputBox['state'] = ('!disabled')
    
def TurnOffOperators():
    MathsOperatorDropdown['state'] = ('disabled')
    SecondInputBox['state'] = ('disabled')
    
#Creates the labels, buttons and input    
InfoLabel = ttk.Label(mainframe, text='Select the correct operation and input the correct numbers before clicking compute')
OutputLabel = ttk.Label(mainframe, textvariable = Output)
ComputeButton = ttk.Button(mainframe, text = 'Compute', command = Compute)
SecondInputBox = ttk.Entry(mainframe, textvariable=SecondNumberToConvert)
InputBox = ttk.Entry(mainframe, textvariable=NumberToConvert)
MathsOperatorDropdown = ttk.Combobox(mainframe, textvariable=MathsOperator)
ConverterDropdown = ttk.Combobox(mainframe, textvariable=Converter)
ConverterDropdown.bind('<<ComboboxSelected>>', ConverterDropdownChanged)
OutputTypeLabel = ttk.Label(mainframe, textvariable = OutputType)
EqualsLabel = ttk.Label(mainframe, text='=')

#Aligns the widgets to a grid
InfoLabel.grid(column=1, row=1, columnspan=4, sticky='N E W S')
InputBox.grid(column=1, row=2, sticky='N E W S')
SecondInputBox.grid(column=3, row=2, sticky='N E W S')
OutputLabel.grid(column=5, row=2, sticky='N E W S')
ComputeButton.grid(column=3, row=3, columnspan=1, sticky='N E W S')
MathsOperatorDropdown.grid(column=2, row=2, sticky='N E W S')
ConverterDropdown.grid(column=1, row=3, columnspan=2, sticky='N E W S')
OutputTypeLabel.grid(column=4, row=3, columnspan=2, sticky='N E W S')
EqualsLabel.grid(column=4, row=2, sticky='N E W S')

#Sets up the dropdown
ConverterDropdown['values'] = ('Convert Decimal to Binary', 'Convert Decimal to Hexadecimal', 'Convert Binary to Decimal', 'Convert Binary to Hexadecimal', 'Convert Hexadecimal to Decimal', 'Convert Hexadecimal to Binary', 'Binary Mathematics', 'Hexadecimal Mathematics')
ConverterDropdown['state'] = ('readonly')
ConverterDropdown.set('Convert Decimal to Binary')

#Resets inputs and outputs
Output.set('0')
OutputType.set('Binary')
MathsOperatorDropdown['values'] = ('+', '-', 'x', '/')
MathsOperatorDropdown.set('+')
MathsOperatorDropdown['state'] = ('disabled')
SecondInputBox['state'] = ('disabled')

#Something to do with the grid. Not 100% sure what it does, but seems needed
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

#Starts the program
root.mainloop();
