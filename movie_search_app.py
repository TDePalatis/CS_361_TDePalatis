#Version 1.0

from tkinter import *

root = Tk()

root.geometry('1000x2500')  # size of screen

title_var = StringVar()
imdbid_var = StringVar()

movieJSON = None


def homepage():
    frame1 = Frame(root, width=1000, height=2500, bg='white')
    frame1.place(x=0, y=0)


    textTitle = Entry(frame1, textvariable = title_var, bd =5)
    textTitle.place(x=150, y=105)

    buttonTitle = Button(frame1, text='Send Request (title)',command=getTitle)
    buttonTitle.place(x=350, y=105)

    textIMDBID = Entry(frame1, textvariable = imdbid_var, bd =5)
    textIMDBID.place(x=150, y=145)

    buttonIMDBID = Button(frame1, text='Send Request (IMDBID)',command=getIMDBID)
    buttonIMDBID.place(x=350, y=145)

    homepageName = Label(frame1, text ="Movie Ticket Counter ")
    homepageName.place(x=300, y=20)

    instructions1 = Label(frame1, text ="Welcome! Please enter either your desired movie title or IMDBID and press the corresponding Send Request.")
    instructions1.place(x=30, y=40)

    instructions2 = Label(frame1,text="Then press Print your ticket and and we will give you your information!")
    instructions2.place(x=150, y=60)


    buttonPrintTicket = Button(frame1, text='Print your Ticket', command=moviePage)
    buttonPrintTicket.place(x=350, y=185)

    buttonWrongTest = Button(frame1, text='oops', command=errorPage)
    buttonWrongTest.place(x=200, y=185)


def getTitle():
    title = title_var.get()

    titleURL = "http://www.omdbapi.com/?t=" + title + "&apikey=7b779361"

    print(titleURL)

    "Connect to internet - get JSON file, dump text to movieData"

def getIMDBID():
    IMDBID = imdbid_var.get()

    imdbidURL = "http://www.omdbapi.com/?i=" + IMDBID + "&apikey=7b779361"

    print(imdbidURL)

    "Connect to internet - get JSON file, dump text to movieData"


def moviePage():
    frame2 = Frame(root, width=1000, height=2500, bg='grey')
    frame2.place(x=0, y=0)

    buttonHome = Button(frame2, text='Return Home', command=homepage)
    buttonHome.place(x=10, y=25)

    moviePageName = Label(frame2, text= "(movie info will be here) ")
    moviePageName.place(x=200, y=20)




def errorPage():
    frame3 = Frame(root, width=1000, height=2500, bg='red')
    frame3.place(x=0, y=0)

    buttonHome = Button(frame3, text='Return Home', command=homepage)
    buttonHome.place(x=10, y=10)

    errorMessage = Label(frame3, text = "Oops! It looks like there was a problem with your ticket! Click the Return Home button to try again! ")
    errorMessage.place(x=200, y=20)


homepage()

root.mainloop()





