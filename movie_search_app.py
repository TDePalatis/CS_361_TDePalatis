#Version 1.0

import time

import json

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
    textTitle.place(x=150, y=75)

    buttonTitle = Button(frame1, text='Get Ticket',command=getTitle)
    buttonTitle.place(x=350, y=75)


    homepageName = Label(frame1, text ="Movie Ticket Counter ")
    homepageName.place(x=200, y=20)

    instructions = Label(frame1, text ="Welcome! Please enter either your desired movie title or IMDBID, and we will give you your ticket!")
    instructions.place(x=30, y=40)


def getTitle():
    title = title_var.get()

    if title[0] == "t" and  title[1] == "t":
        URL = "http://www.omdbapi.com/?i=" + title + "&apikey=7b779361"

    else:
        URL = "http://www.omdbapi.com/?t=" + title + "&apikey=7b779361"


    f = open('movie_request.txt', 'w')
    f.write(URL)
    f.close()

    time.sleep(3)


    #Partner Microservice occurs here - it will use the URL to search for a JSON file and then return said file.


    with open('movie_data.json', 'r') as infile:
        movieData = json.load(infile)


    if movieData["Response"] == "True":
        return moviePage()
    else:
        return errorPage()


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
