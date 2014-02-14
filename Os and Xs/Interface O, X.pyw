#Imports needed librarys
#import tkinter
import random
import math
from tkinter import *
from tkinter import ttk


#Initiates the GUI
root = Tk()
root.title("Noughts And Crosses")

#Creates the picture variables
PicBlank = PhotoImage(file='Blank.gif')
PicO = PhotoImage(file='O.gif')
PicX = PhotoImage(file='X.gif')

#Creates the frame to hold everything
mainframe = ttk.Frame(root, borderwidth=5, relief="flat", width=200, height=100, padding = "23 23 23 23")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Initiates some variables
ScoreVar = StringVar() #String for the label to show the score on the GUI
ScoreVal = 0 #Holds the current score
TempScore = 0 #Used for temp storage of the score

Turns = 0 #Turns done by the AI. Used to determine a draw.
B = [0,0,0,0,0,0,0,0,0,0] #Who owns each button
win = False

#Saves the score (With encryption :D)
def Save():
    global ScoreVal
    TempString = str((ScoreVal * ScoreVal)/7)
    text_file = open("Score.txt","w")    
    text_file.write(TempString)
    text_file.close()
    
#Loads and unencrypts the score
def Load():
    global ScoreVal
    global ScoreVar
    text_file = open("Score.txt", "r")
    TempString = text_file.read()
    ScoreVal = int(math.sqrt((float(TempString)*7)))
    ScoreVar.set(ScoreVal)
    text_file.close()

#The AI. Rather simple but works. It checks whether
#it can win, then if you can win, and if neither, puts it in a random spot.
def AI():
    global win
    if win == False:
        #Vertical, Column 1
        if B[1] == 2 and B[2] == 2 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            win2()
        elif B[1] == 2 and B[3] == 2 and B[2] == 0:
            B[2] = 2
            button2['image'] = PicO
            win2()
        elif B[2] == 2 and B[3] == 2 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            win2()

        #Vertical, Column 2
        elif B[4] == 2 and B[5] == 2 and B[6] == 0:
            B[6] = 2
            button6['image'] = PicO
            win2()
        elif B[4] == 2 and B[6] == 2 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            win2()
        elif B[5] == 2 and B[3] == 2 and B[4] == 0:
            B[4] = 2
            button4['image'] = PicO
            win2()

        #Vertical, Column 3
        elif B[7] == 2 and B[8] == 2 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            win2()
        elif B[7] == 2 and B[9] == 2 and B[8] == 0:
            B[8] = 2
            button8['image'] = PicO
            win2()
        elif B[8] == 2 and B[9] == 2 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO
            win2()
            
        #Horizontal, Row 1
        elif B[1] == 2 and B[4] == 2 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO
            win2()
        elif B[7] == 2 and B[4] == 2 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            win2()
        elif B[1] == 2 and B[7] == 2 and B[4] == 0:
            B[4] = 2
            button4['image'] = PicO
            win2()
            
        #Horizontal, Row 2
        elif B[2] == 2 and B[5] == 2 and B[8] == 0:
            B[8] = 2
            button8['image'] = PicO
            win2()
        elif B[8] == 2 and B[5] == 2 and B[2] == 0:
            B[2] = 2
            button2['image'] = PicO
            win2()
        elif B[2] == 2 and B[8] == 2 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            win2()
            
        #Horizontal, Row 3
        elif B[3] == 2 and B[6] == 2 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            win2()
        elif B[9] == 2 and B[6] == 2 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            win2()
        elif B[3] == 2 and B[9] == 2 and B[6] == 0:
            B[6] = 2
            button6['image'] = PicO
            win2()
            
        #Diagonal, Top left to Bottom Right
        elif B[1] == 2 and B[5] == 2 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            win2()
        elif B[9] == 2 and B[5] == 2 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            win2()
        elif B[1] == 2 and B[9] == 2 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            win2()
            
        #Diagonal, Top Right to Bottom Left
        elif B[7] == 2 and B[5] == 2 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            win2()
        elif B[7] == 2 and B[3] == 2 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            win2()
        elif B[3] == 2 and B[5] == 2 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO
            win2()



        #Vertical, Column 1
        elif B[1] == 1 and B[2] == 1 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            
        elif B[1] == 1 and B[3] == 1 and B[2] == 0:
            B[2] = 2
            button2['image'] = PicO
            
        elif B[2] == 1 and B[3] == 1 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            

        #Vertical, Column 2
        elif B[4] == 1 and B[5] == 1 and B[6] == 0:
            B[6] = 2
            button6['image'] = PicO
            
        elif B[4] == 1 and B[6] == 1 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            
        elif B[5] == 1 and B[6] == 1 and B[4] == 0:
            B[4] = 2
            button4['image'] = PicO
            

        #Vertical, Column 3
        elif B[7] == 1 and B[8] == 1 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            
        elif B[7] == 1 and B[9] == 1 and B[8] == 0:
            B[8] = 2
            button8['image'] = PicO
            
        elif B[8] == 1 and B[9] == 1 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO
            
            
        #Horizontal, Row 1
        elif B[1] == 1 and B[4] == 1 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO
            
        elif B[7] == 1 and B[4] == 1 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            
        elif B[1] == 1 and B[7] == 1 and B[4] == 0:
            B[4] = 2
            button4['image'] = PicO
            
            
        #Horizontal, Row 2
        elif B[2] == 1 and B[5] == 1 and B[8] == 0:
            B[8] = 2
            button8['image'] = PicO
            
        elif B[8] == 1 and B[5] == 1 and B[2] == 0:
            B[2] = 2
            button2['image'] = PicO
            
        elif B[2] == 1 and B[8] == 1 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            
            
        #Horizontal, Row 3
        elif B[3] == 1 and B[6] == 1 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            
        elif B[9] == 1 and B[6] == 1 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            
        elif B[3] == 1 and B[9] == 1 and B[6] == 0:
            B[6] = 2
            button6['image'] = PicO
            
            
        #Diagonal, Top left to Bottom Right
        elif B[1] == 1 and B[5] == 1 and B[9] == 0:
            B[9] = 2
            button9['image'] = PicO
            
        elif B[9] == 1 and B[5] == 1 and B[1] == 0:
            B[1] = 2
            button1['image'] = PicO
            
        elif B[1] == 1 and B[9] == 1 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            
            
        #Diagonal, Top Right to Bottom Left
        elif B[7] == 1 and B[5] == 1 and B[3] == 0:
            B[3] = 2
            button3['image'] = PicO
            
        elif B[7] == 1 and B[3] == 1 and B[5] == 0:
            B[5] = 2
            button5['image'] = PicO
            
        elif B[3] == 1 and B[5] == 1 and B[7] == 0:
            B[7] = 2
            button7['image'] = PicO

            
        #The Random place   
        else:
            loop = 1
            while loop == 1:
                place = random.randrange(1, 10)
                if B[place] == 0:
                    loop = 0
                    B[place] = 2
                    if place == 1:
                        button1['image'] = PicO
                        
                    elif place == 2:     
                        button2['image'] = PicO
                        
                    elif place == 3:       
                        button3['image'] = PicO
                        
                    elif place == 4:
                        button4['image'] = PicO
                        
                    elif place == 5:
                        button5['image'] = PicO
                        
                    elif place == 6:
                        button6['image'] = PicO
                        
                    elif place == 7:
                        button7['image'] = PicO
                        
                    elif place == 8:
                        button8['image'] = PicO
                        
                    elif place == 9:
                        button9['image'] = PicO
                    

#The def that executes when you win
def win1():
    global ScoreVal
    global ScoreVar
    global win
    win = True
    ScoreVal = ScoreVal + 1
    ScoreVar.set(ScoreVal)
    Save()
    
#The def that happens when the AI wins
def win2():
    global win
    global ScoreVal
    global ScoreVar
    win = True
    ScoreVal = ScoreVal - 1
    ScoreVar.set(ScoreVal)
    Save()

#The def that executes in the event of a draw
def Draw():
    Restart.state(['!disabled'])

#Creates the button functions. Calls the appropriate check module
#Button 1, 1
def Button1():
    global win
    global B
    global Turns
    if B[1] == 0 and win == False:
        Turns = Turns + 1
        button1['image'] = PicX
        B[1] = 1
        if (B[2] == 1 and B[3] == 1) or (B[7] == 1 and B[4] == 1) or (B[5] == 1 and B[9] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 1, 2
def Button2():
    global win
    global B
    global Turns
    if B[2] == 0 and win == False:
        Turns = Turns + 1
        B[2] = 1
        button2['image'] = PicX
        if (B[1] == 1 and B[3] == 1) or (B[8] == 1 and B[5] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 1, 3
def Button3():
    global B
    global win
    global Turns
    if B[3] == 0 and win == False:
        Turns = Turns + 1
        B[3] = 1
        button3['image'] = PicX
        if (B[2] == 1 and B[1] == 1) or (B[7] == 1 and B[5] == 1) or (B[6] == 1 and B[9] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 2, 1
def Button4():
    global B
    global win
    global Turns
    if B[4] == 0 and win == False:
        Turns = Turns + 1
        B[4] = 1
        button4['image'] = PicX
        if (B[5] == 1 and B[6] == 1) or (B[7] == 1 and B[1] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 2, 2
def Button5():
    global B
    global win
    global Turns
    if B[5] == 0 and win == False:
        Turns = Turns + 1
        B[5] = 1
        button5['image'] = PicX
        if (B[2] == 1 and B[8] == 1) or (B[6] == 1 and B[4] == 1) or (B[1] == 1 and B[9] == 1) or (B[7] == 1 and B[3] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 2, 3
def Button6():
    global B
    global win
    global Turns
    if B[6] == 0 and win == False:
        Turns = Turns + 1
        B[6] = 1
        button6['image'] = PicX
        if (B[9] == 1 and B[3] == 1) or (B[5] == 1 and B[4] == 1):
            win1() 
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 3, 1
def Button7():
    global B
    global win
    global Turns
    if B[7] == 0 and win == False:
        Turns = Turns + 1
        B[7] = 1
        button7['image'] = PicX
        if (B[1] == 1 and B[4] == 1) or (B[8] == 1 and B[9] == 1) or (B[5] == 1 and B[3] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 3, 2
def Button8():
    global B
    global win
    global Turns
    if B[8] == 0 and win == False:
        Turns = Turns + 1
        B[8] = 1
        button8['image'] = PicX
        if (B[2] == 1 and B[5] == 1) or (B[7] == 1 and B[9] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()
#Button 3, 3
def Button9():
    global B
    global win
    global Turns
    if B[0] == 0 and win == False:
        Turns = Turns + 1
        B[9] = 1
        button9['image'] = PicX
        if (B[6] == 1 and B[3] == 1) or (B[7] == 1 and B[8] == 1) or (B[5] == 1 and B[1] == 1):
            win1()
        elif Turns < 9:
            Turns = Turns + 1
            AI()
        else:
            Draw()

#The def that is called to restart the program
def Restart():
    global B
    global win
    global Turns
    Turns = 0
    win = False
    B[1] = 0
    B[2] = 0
    B[3] = 0
    B[4] = 0
    B[5] = 0
    B[6] = 0
    B[7] = 0
    B[8] = 0
    B[9] = 0
    button1["image"] = PicBlank
    button2["image"] = PicBlank
    button3["image"] = PicBlank
    button4["image"] = PicBlank
    button5["image"] = PicBlank
    button6["image"] = PicBlank
    button7["image"] = PicBlank
    button8["image"] = PicBlank
    button9["image"] = PicBlank    

#The def that executes when the'Exit' button
#is clicked. As expected, it exits the program.
def Exit():
    Save()
    root.destroy()
    
#Creates the buttons
button1 = ttk.Button(mainframe, command=Button1)
button2 = ttk.Button(mainframe, command=Button2)
button3 = ttk.Button(mainframe, command=Button3)
button4 = ttk.Button(mainframe, command=Button4)
button5 = ttk.Button(mainframe, command=Button5)
button6 = ttk.Button(mainframe, command=Button6)
button7 = ttk.Button(mainframe, command=Button7)
button8 = ttk.Button(mainframe, command=Button8)
button9 = ttk.Button(mainframe, command=Button9)
Restart = ttk.Button(mainframe, text='Restart', command=Restart)
Exit = ttk.Button(mainframe, text='Exit', command=Exit)
Score = ttk.Label(mainframe, textvariable=ScoreVar)

button1["image"] = PicBlank
button2["image"] = PicBlank
button3["image"] = PicBlank
button4["image"] = PicBlank
button5["image"] = PicBlank
button6["image"] = PicBlank
button7["image"] = PicBlank
button8["image"] = PicBlank
button9["image"] = PicBlank  

#Aligns the buttons in a grid
button1.grid(column=1, row=1)
button2.grid(column=1, row=2)
button3.grid(column=1, row=3)
button4.grid(column=2, row=1)
button5.grid(column=2, row=2)
button6.grid(column=2, row=3)
button7.grid(column=3, row=1)
button8.grid(column=3, row=2)
button9.grid(column=3, row=3)
Restart.grid(column=1, row=5)
Exit.grid(column=2, row=5)
Score.grid(column=3, row=5)

#Actually loads the score
Load()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

root.mainloop();
