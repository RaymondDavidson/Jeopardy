#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jeopardy-tk.py
#
#  Copyright 2017 Chelsea School Students and Rik Goldman <rgoldman@chelseaschool.edu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

# the pound or hash symbol means a 1 line comment follows; comments are ignored by the interpreter

"""
Jeopardy style quiz about civil rights leaders often not included in curriculum.

Summary:

    This is a program written in Python. It...
"""

#### Dependencies ####
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import sys
import ttk as ttk
import shelve
import webbrowser
import time
import os
import subprocess

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]


    #### Lists ####

    # people who worked on this project (in list format)
    # TODO: move to documentation
    # credits = ["Ocho262", "FlamboyantPapayas", "ghoulmann", "Sidhant", "IHopRocks", "Raymond R. Davidson", "RC", "EB", "MS", "Shaun"]

    """
    These are the prompts in the game that
    players answer (in the form of a question)

    """

    question = [
        "She is a civil-rights activist that argued for the abolition of prisons.\n\n",
        "He is the civil-rights leader who described potentially radical action in support of civil rights progress as \"marvelous new militancy\".\n\n",
        "She is a civil-rights activist that argued \"We have nothing to lose but our chains.\"\n\n",
        "He believed \"a riot is the voice of the unheard.\"\n\n",
        "He was the lawyer to Malcom X. \n\n",
        "She believed that freedom is only earned every generation.\n\n",
        "This activist said that, \"Hate is too great a burden to bear. It injures the hater more than it injures the hated.\"\n\n",
        "Who believed that \"all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation.\"\n\n",
        "She said \"It is our duty to fight for our freedom. It is our duty to win. We must love each other and support each other. We have nothing to lose but our chains.\"\n\n",
        "According to him, \"The revolution has always been in the hands of the young. The young inherit the revolution.\"\n\n",
        "She said \"No one is going to give you the education you need to overthrow them.\"\n\n",
        "She said  \"It is our duty to fight for our freedom. It is our duty to win.\"\n\n",
        "He said \"You don't fight racism with racism, the best way to fight racism is with solidarity.\"\n\n",
        "He said \"You can jail a revolutionary, but you can not jail the revolution.\"\n\n",
        "She said \"I don't believe you can stand for freedom  for one group of people and deny it to others.\"\n\n",
        "She makes clear that \"the political core of any movement for freedom in the society has to have the political imperative to protect free speech.\"\n\n",
        "He wrote \"the secret of life is to have no fear; it's the only way to function.\"\n\n",
        "She said \"I will not have my life narrowed down. I will not bow down to somebody else's whim or to someone else's ignorance.\"\n\n",
        "He said \"If you see something that is not right, not fair, not just, you have a moral obligation to do something about it.\"\n\n",
        "She said, \"being oppressed means the absence of choices.\"\n\n",
        "She said, \"I want there to be a place in the world where people can engage in one another's differences in a way that is redemptive, full of hope and possibility. Not this \'In order to love you, I must make you something else\'. That's what domination is all about, that in order to be close to you, I must possess you, remake and recast you.\"\n\n",
        "He said, \"The civil rights movement was based on faith. Many of us who were participants in this movement saw our involvement as an extension of our faith. We saw ourselves doing the work of the Almighty. Segregation and racial discrimination were not in keeping with our faith, so we had to do something.\"\n\n",
        "He said, 'Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.\"\n\n",
        "She said that, \"hate is too great a burden to bear. It injures the hater more than it injures the hated.\"\n\n",
        "She believed that \"all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation.\"\n\n",
        "She said \"this is the 21st century; we need to redefine revolution.\"\n\n",
        "He said \"Don't give up, Don't give out, Don't give in.\"\n\n",
        "She said \"Feminism is for everybody.\"\n\n",
        "She said \"radical\" simply means \"grasping by the roots.\"\n\n"
    ]


    # This is a Python list.
    # Answers that match the above questions (in same order).
    answer = [
        "Who is Dr. Angela Davis?",
        "Who is Dr. Martin Luther King, Jr.?",
        "Who is Assata Shakur?",
        "Who is Dr. Martin Luther King, Jr.?",
        "Who is Percy Sutton?",
        "Who is Coretta Scott King?",
        "Who is Coretta Scott King?",
        "Who is Coretta Scott King?",
        "Who is Assata Shakur?",
        "Who is Huey P. Newton?",
        "Who is Assata Shakur?",
        "Who is Assata Shakur?",
        "Who is Bobby Seale?",
        "Who is Bobby Seale?",
        "Who is Coretta Scott King?",
        "Who is bell hooks?",
        "Who is Stokely Carmichael?",
        "Who is bell hooks?",
        "Who is Rep. John Lewis?",
        "Who is bell hooks?",
        "Who is bell hooks?",
        "Who is Rep. John Lewis?",
        "Who is Dr. Martin Luther King, Jr.?",
        "Who is Coretta Scott King?",
        "Who is Coretta Scott King?",
        "Who is Assata Shakur?",
        "Who is Rep. John Lewis?",
        "Who is bell hooks?",
        "Who is Dr. Angela Davis?"
    ]




    #### Variables ####



    global fontFace, correct, ques, count, title, fontFace, browserName, correct, ques, count, entry, further, root, browserName
    #### Functions Section ######


    #def askGoogle(string, browserName):
    def askGoogle(string):
        """In case of wrong answer, show correct person from google search.

        Turns correct answer in to a google ask, and then opens a browser tab to the google search results in a new tab. Process is dependent on OS.name.

        Currently browser is set to firefox and confirmed to work, as long as firefox is installed.

        Args
        ----

        string (str):
            The question to look up (from the list)
        browserName (str):
            browser defined in the variables (line 142)

        Returns
        -------

            bool: True for success. False otherwise.

        .. TODO::
            var platform is duplicated. Find a solution without repetition.
        """
        ask = string
        ask = ask.replace(" ", "+")
        www = "https://www.google.com/#q=" + ask + "&*"
        platform = os.name
        if platform == "posix":
            try:
                #web = webbrowser.get(browserName)
                ask = string
                ask = ask.replace(" ", "+")
                www = "https://www.google.com/#q=" + ask + "&*"
                webbrowser.open(www, new=0, autoraise=False)
                #web.open(www, new=0, autoraise=False)
            except:
                print "We're sorry; we couldn't show the answer with a browser."
        else:
            try:
                webbrowser.open(www, new=0, autoraise=False)
            except:
                print "Couldn't raise a browser."


    def pop(title, string):
        msg = tkMessageBox
        msg = msg.showinfo(title, string)


    #def killBrowser(browserName):
    #    platform = os.name
    #    if platform == 'nt':
    #        try:
    #            os.system("taskkill /im firefox.exe")
    #        except:
    #            print "Couldn't close browser. We're sorry."
    #    else:
    #        try:
    #            print subprocess.check_output('kill -15 $(ps ax | grep ' + browserName + ' | grep -v grep | awk \'{print $1}\')',shell=True)
    #        except:
    #            print "Subprocess could not kill firefox."


    # function for continuing
    def out(*event):

        global correct, ques, count, entry, further, root, browserName
        entry.focus()
        further["value"] = ques
        ans = entry.get()
        if ques < count:
            entry.focus()
            further["value"] = ques
            further.pack()
            if ans == answer[ques]:
                correct = correct + 1
                ques = ques + 1
                entry.delete(0, END)
                label.config(text = question[ques])
                score.config(text=("Score: " + str(correct) + "/" + str(ques)))

            else:
                askGoogle(answer[ques])
                #askGoogle(answer[ques], browserName)
                root.after(0500, lambda:root.focus_force())
                entry.focus()
                ques = ques + 1
                entry.delete(0, END)
                entry.focus()
        if ques < count:
            label.config(text = question[ques])
            score.config(text=("Score: " + str(correct) + "/" + str(ques)))
        else:
            close()

    def widgets():
        global fontFace, further, entry, label, score

        #frame inside window to control bottom element layout
        bottomframe = Frame(root)
        bottomframe.pack( side = BOTTOM )
        # midFrame for entry
        midFrame = Frame(root)
        midFrame.pack(side=BOTTOM)

        # root widgets
        dummy(root)

        people = ttk.Label(root,wraplength=500, foreground="red", text="Dr. Angela Davis, Dr. Martin Luther King, Jr., Assata Shakur, bell hooks, Stokely Carmichael, Bobby Seale, Percy Sutton, Coretta Scott King, Huey P. Newton, Rep. John Lewis\n\n")
        people.pack()

        label = ttk.Label(root,text = question[ques],wraplength=300, font=fontFace)
        label.pack()

        # midFrame widgets
        whois = StringVar(root, value='Who is...?')
        entry = ttk.Entry(midFrame, width=40, textvariable=whois)
        entry.focus()
        entry.pack()
        dummy(midFrame)
        # Submit button: to continue game, submit answer (calls out() function)
        submit = tk.Button(midFrame,text = "OK",command = out, fg="white", bg="green")
        submit.pack()
        #below submit button, spacers
        dummy(midFrame)
        dummy(midFrame)
        dummy(midFrame)
        # bottomframe widgets
        #horizontal spacers (calling dummy() function defined above)
        dummy(bottomframe)
        # horizontal spacer: calls dummy() function above
        dummy(bottomframe)

        # current score output
        score = ttk.Label(bottomframe, text = "Score: 0/0", font=fontFace)
        score.pack()
        dummy(bottomframe)
        # make and pack progressbar: (green on windows, grey on linux, striped on mac)
        further = ttk.Progressbar(bottomframe, mode="determinate",orient="horizontal", maximum=count, variable=ques, length=300, value=0)
        further.pack()
        # make label for progressbar
        pb = ttk.Label(bottomframe, text="Progress")
        pb.pack()
        #spacers call the bottomframe() function
        dummy(bottomframe)
        dummy(bottomframe)

        # quit button calls "close" function
        leave = tk.Button(bottomframe,text = "Quit",command = close, fg="white", bg="red")
        leave.pack()
        #spacer
        dummy(bottomframe)

        # Key Binding
        # Keyboard Input
        root.bind('<Return>', out)
        # Use <Escape> to quit using close method
        root.bind('<Escape>', close)


    def close(*event):
        #global root, browserName
        #try:
        #shelf = shelve.open('data/scores.dat') # here you will save the score variable
        #shelf['score'] = str(correct)      # thats all, now it is saved on disk.
        #for points in shelf['score']:
        #    print(points)
        #shelf.close() # closes the db file with scores
        # Test kill broser if its firefox running on posix arch
        #print subprocess.check_output('kill $(ps ax | grep firefox | grep -v grep | awk \'{print $1}\')',shell=True)


        # Kills the Brower: essential - otherwise the close dialog is invisible
        #killBrowser(browserName)

        root.after(40000, lambda: root.destroy())
        pop("Thank you", "Thank you for learning with us!")
        #root.focus_force()
        root.destroy()

    def dummy(parent):
        spacer = ttk.Label(parent, text = " ")
        spacer.pack()



    # creates root window
    # Set Variables (variables represent values that change)
    correct = 0
    ques = 0
    count = len(answer)
    title = "Protest & Resist (Power to the People!)"
    fontFace = 'arial 15 bold'
    #browserName = 'firefox'
    root = tk.Tk()
    # sets geometry for root window
    root.geometry('{}x{}'.format(600, 700))
    #name at top of dialog
    windowtitle = root.wm_title(title)
    widgets()
    # Create splash dialog (message box)
    splash = pop("Welcome", "Protest & Resist (Power to the People!)\n\nEnter your answers in the form of a question (like Jeopardy) -- Capitalization, spelling, and punctuation count. At the top of the game, you'll see possible answers. Press 'OK' to submit an answer; press 'Quit' to end the game.\n")
    root.attributes('-topmost', True)
    root.mainloop()

if __name__ == "__main__":
    main()
