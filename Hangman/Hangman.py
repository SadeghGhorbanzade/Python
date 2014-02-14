import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Initiates the GUI
root = Tk()
root.title("Hangman")
root.resizable(FALSE,FALSE)

#Creates the frames to hold everything
wordframe = ttk.Frame(root, borderwidth=5, relief="flat", width=200, height=100, padding = "10 10 10 10")
wordframe.grid(column=0, row=0, sticky=(N, W, S, E))

#Variables
scoreVar = StringVar()
wordVar = StringVar()
wrong = 0
score = 0
word = ''
guessedWord = []
letterDict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
wordDict = []

for line in open("Dictionary.txt", "r"):
    wordDict.append(line)
    
#widgets
LetterButtons = []

def letter(letter):
    global LetterButtons
    global word
    global score
    global wrong
    global guessedWord
    for i in range(1,27):
        if letterDict[i] == letter:
            tempInt = i-1
    LetterButtons[tempInt].state(['disabled'])
    tempStr = ''
    tempFlag = False
    for i in range(len(word)):
        if word[i] == letter:
            tempFlag = True
            guessedWord[i] = word[i]
    for item in guessedWord:
        tempStr+=item
    wordVar.set(tempStr)
    if tempFlag == False:
        wrong+=1
        hangmanImage['image'] = hangman[wrong]
        if wrong >= 9:
            for i in range(26):
                LetterButtons[i].state(['disabled'])
            newGameButton.state(['!disabled'])
            wordVar.set(word)
            score-=1
            scoreVar.set(score)
    if tempStr == word:
        score+=1
        scoreVar.set(score)
        for i in range(26):
            LetterButtons[i].state(['disabled'])
        newGameButton.state(['!disabled'])
    
def newGame():
    global wrong
    for i in range(26):
        LetterButtons[i].state(['!disabled'])
    newGameButton.state(['disabled'])
    wrong = 0
    hangmanImage['image'] = hangman[wrong]                     
    createWord()

def createWord():
    global word
    global guessedWord
    tempStr = ''
    guessedWord = []
    word = wordDict[random.randrange(len(wordDict))]
    word = word.rstrip()
    word = word.upper()
    for i in range(len(word)):
        guessedWord.append('*')
    for item in guessedWord:
        tempStr+=item
    wordVar.set(tempStr)

#Images
hangman = []
for i in range(1, 11):
    tempStr = 'Image'+str(i)+'.gif'
    hangman.append(PhotoImage(file=tempStr))

#Hangman
hangmanImage = ttk.Label(wordframe, image=hangman[wrong])
hangmanImage.grid(column=0, row=0, columnspan=7, sticky='N')

#Letters
LetterButtons.append(ttk.Button(wordframe, text = 'A', command = lambda: letter('A')))
LetterButtons.append(ttk.Button(wordframe, text = 'B', command = lambda: letter('B')))
LetterButtons.append(ttk.Button(wordframe, text = 'C', command = lambda: letter('C')))
LetterButtons.append(ttk.Button(wordframe, text = 'D', command = lambda: letter('D')))
LetterButtons.append(ttk.Button(wordframe, text = 'E', command = lambda: letter('E')))
LetterButtons.append(ttk.Button(wordframe, text = 'F', command = lambda: letter('F')))
LetterButtons.append(ttk.Button(wordframe, text = 'G', command = lambda: letter('G')))
LetterButtons.append(ttk.Button(wordframe, text = 'H', command = lambda: letter('H')))
LetterButtons.append(ttk.Button(wordframe, text = 'I', command = lambda: letter('I')))
LetterButtons.append(ttk.Button(wordframe, text = 'J', command = lambda: letter('J')))
LetterButtons.append(ttk.Button(wordframe, text = 'K', command = lambda: letter('K')))
LetterButtons.append(ttk.Button(wordframe, text = 'L', command = lambda: letter('L')))
LetterButtons.append(ttk.Button(wordframe, text = 'M', command = lambda: letter('M')))
LetterButtons.append(ttk.Button(wordframe, text = 'N', command = lambda: letter('N')))
LetterButtons.append(ttk.Button(wordframe, text = 'O', command = lambda: letter('O')))
LetterButtons.append(ttk.Button(wordframe, text = 'P', command = lambda: letter('P')))
LetterButtons.append(ttk.Button(wordframe, text = 'Q', command = lambda: letter('Q')))
LetterButtons.append(ttk.Button(wordframe, text = 'R', command = lambda: letter('R')))
LetterButtons.append(ttk.Button(wordframe, text = 'S', command = lambda: letter('S')))
LetterButtons.append(ttk.Button(wordframe, text = 'T', command = lambda: letter('T')))
LetterButtons.append(ttk.Button(wordframe, text = 'U', command = lambda: letter('U')))
LetterButtons.append(ttk.Button(wordframe, text = 'V', command = lambda: letter('V')))
LetterButtons.append(ttk.Button(wordframe, text = 'W', command = lambda: letter('W')))
LetterButtons.append(ttk.Button(wordframe, text = 'X', command = lambda: letter('X')))
LetterButtons.append(ttk.Button(wordframe, text = 'Y', command = lambda: letter('Y')))
LetterButtons.append(ttk.Button(wordframe, text = 'Z', command = lambda: letter('Z')))
for x in range(1,27):    
    if x <= 7:
        LetterButtons[x-1].grid(column=x-1, row=3, sticky='N E W S')
    elif x <= 14:
        LetterButtons[x-1].grid(column=x-8, row=4, sticky='N E W S')
    elif x <= 21:
        LetterButtons[x-1].grid(column=x-15, row=5, sticky='N E W S')
    else:
        LetterButtons[x-1].grid(column=x-22, row=6, sticky='N E W S')
for i in range(26):
        LetterButtons[i].state(['disabled'])
        
#New Game button
newGameButton = ttk.Button(wordframe, text = 'New Game', command = newGame)
newGameButton.grid(column=5, row=6, sticky='N E W S')
scoreLabel = ttk.Label(wordframe, textvariable = scoreVar)
scoreLabel.grid(column=6, row=6)

#Word Variable
wordLabel = ttk.Label(wordframe, textvariable = wordVar, font=("Times", 36, "bold"))
wordLabel.grid(column=0, row=1, columnspan=7, sticky='N')

scoreVar.set(score)
wordVar.set('Press new game to start!')

#Something to do with the grid. Not 100% sure what it does, but seems needed
for child in wordframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>')

#Starts the program
root.mainloop();
