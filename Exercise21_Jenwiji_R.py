from tkinter import *
import math

def leftClick(event):
    result = float(textboxw.get())/math.pow(float(textboxh.get())/100, 2)
    print(result)
    if (result>=30):
        labeloutput.configure(text = "Very Obese")
    elif (25.0<=result<=29.9):
        labeloutput.configure(text = "Obese")
    elif (23.0<=result<=24.9):
        labeloutput.configure(text = "Overweight")
    elif (18.6<=result<=22.9):
        labeloutput.configure(text = "Normal")
    elif (result<=18.5):
        labeloutput.configure(text = "Underweight")
    #labeloutput.configure(text = (float(textboxw.get())/math.pow(float(textboxh.get())/100, 2)))

mainWindow = Tk('Welcome to BMI calculator')

labelheight = Label(mainWindow, text = 'Height in CM')
labelheight.grid(row=0, column=0)
textboxh = Entry(mainWindow)
textboxh.grid(row=0, column=1)

labelweight = Label(mainWindow, text = 'Weight in KG')
labelweight.grid(row=1, column=0)
textboxw = Entry(mainWindow)
textboxw.grid(row=1, column=1)

calcbutton = Button(mainWindow, text = 'Calculate My BMI')
calcbutton.bind('<Button-1>',  leftClick)
calcbutton.grid(row=2, column=0)

labeloutput = Label(mainWindow, text = 'result')
labeloutput.grid(row=2, column=1)
mainWindow.mainloop()