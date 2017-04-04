#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jeopardy_quiz.py

# == Preface ==

# === Copyright ===

#  Copyright 2017 Chelsea School Students and Rik Goldman <rgoldman@chelseaschool.edu>

# === License ===

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

# the pound or hash symbol means a 1 line comment follows; comments are
# ignored by the interpreter



# ==Introduction ==

#Jeopardy style quiz about civil rights leaders often not included in curriculum.

# === Summary ===

"""
This is a program written in Python. It seeks to teach students about historically significant perspectives on civil rights that are not part of the high-school or middle-school curriculum.

It asks questions that are answered jeopardy-style. Each question that is answered incorrectly opens a browser tab with correct information.
"""

# == Code ==

# === Dependencies ===

# Import Libraries
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import sys
import ttk as ttk
import webbrowser
import time
import os
import subprocess

# === Functions ===


def askGoogle(string):
    """
    In case of wrong answer, show correct 'person' from google search.

    Turns correct answer into a google ask, and then opens a browser tab to the google search results.

    Relies on default browser of the system to improve compatibility.



    :param string: The question to look up (from the list)
    :type string: str

    :returns: True for success. False otherwise.
    :rtype: bool

    """

    ask = string
    ask = ask.replace(" ", "+")
    www = "https://www.google.com/#q=" + ask + "&*"

    # Lines 90 - 100 unnecessary and should be removed
    platform = os.name
    if platform == "posix":
        try:
            webbrowser.open(www, new=0, autoraise=False)
        except BaseException:
            print("We're sorry; we couldn't show the answer with a browser.")
    else:
        try:
            webbrowser.open(www, new=0, autoraise=False)
        except BaseException:
            print("Couldn't raise a browser.")


def pop(title, string):
    """
    We used three pop-up message boxes in the course of development.
    We don't repeat ourselves, so we just called this function each
    time we need a messagebox to appear.


    :param title: Title of the dialog
    :type title: str

    :param string: message of the messagebox
    :type string: str

    :rtype: bool
    """
    msg = tkMessageBox
    msg = msg.showinfo(title, string)

# function for continuing (on correct or incorrect answer)
def out(*event):
    """
    Output contents to window "root"

    Output to the main window. Changes after each answer is submitted, until there are no questions left to answer.


    :param event: Optional. How to work with <Enter> key stroke or Submit button being pressed.
    :type event: event - on button click or <Enter> key
    :rtype: bool
    """
    global correct, ques, count, entry, further, root, browserName

    # bring cursor to the input field
    entry.focus()
    # change progress bar
    further["value"] = ques
    # process input
    ans = entry.get()
    # conditional: if still questions left to answer, do the things that
    # follow.
    if ques < count:
        entry.focus()
        further["value"] = ques
        further.pack()
        # conditional: if answer is correct, increase score, change
        # question.
        if ans == answer[ques]:
            correct = correct + 1
            ques = ques + 1
            entry.delete(0, END)
            label.config(text=question[ques])
            score.config(text=("Score: " + str(correct) + "/" + str(ques)))
        # if not correct answer, do what follows.
        else:
            askGoogle(answer[ques])
            root.after(0o500, lambda: root.focus_force())
            entry.focus()
            ques = ques + 1
            entry.delete(0, END)
            entry.focus()

    # if there are questions left, go to next question
    # TODO: Check throughly that this is not redundant
    if ques < count:
        label.config(text=question[ques])
        score.config(text=("Score: " + str(correct) + "/" + str(ques)))
    # if no more questions, close program.
    else:
        # call the close function with no parameters
        close()

# This function contains all the widget directives for root, bottomframe and midFrame
def widgets():
    """
    Adds windgets to window

    Function for adding all the widgets to the graphical user interface. Also sets up two frames for the lower 2/3 of frames.


    :rtype: bool: True if successful
    """

    # a declaration of globals that will be required by the function
    global fontFace, further, entry, label, score, question

    # frame inside window to control bottom element layout
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)
    # midFrame for entry
    midFrame = Frame(root)
    midFrame.pack(side=BOTTOM)

    # ==== root widgets ====

    dummy(root)

    people = ttk.Label(
        root,
        wraplength=500,
        foreground="red",
        text="Dr. Angela Davis, Dr. Martin Luther King, Jr., Assata Shakur, bell hooks, Stokely Carmichael, Bobby Seale, Percy Sutton, Coretta Scott King, Huey P. Newton, Rep. John Lewis\n\n")
    people.pack()

    label = ttk.Label(
        root,
        text=question[ques],
        wraplength=300,
        font=fontFace)
    label.pack()

    # ==== midFrame widgets ====
    whois = StringVar(midFrame, value='Who is...?')
    entry = ttk.Entry(midFrame, width=40, textvariable=whois)
    entry.focus()
    entry.pack()
    dummy(midFrame)
    # Submit button: to continue game, submit answer (calls out() function)
    submit = tk.Button(
        midFrame,
        text="OK",
        command=out,
        fg="white",
        bg="green")
    submit.pack()
    # below submit button, spacers
    dummy(midFrame)
    dummy(midFrame)
    dummy(midFrame)

    # ==== bottomframe widgets ====

    # horizontal spacers (calling dummy() function defined above)
    dummy(bottomframe)
    # horizontal spacer: calls dummy() function above
    dummy(bottomframe)

    # current score output
    score = ttk.Label(bottomframe, text="Score: 0/0", font=fontFace)
    score.pack()
    dummy(bottomframe)
    # make and pack progressbar: (green on windows, grey on linux, striped on mac)
    further = ttk.Progressbar(
        bottomframe,
        mode="determinate",
        orient="horizontal",
        maximum=count,
        variable=ques,
        length=300,
        value=0)
    further.pack()
    # make label for progressbar
    pb = ttk.Label(bottomframe, text="Progress")
    pb.pack()
    # spacers call the bottomframe() function
    dummy(bottomframe)
    dummy(bottomframe)

    # quit button calls "close" function
    leave = tk.Button(
        bottomframe,
        text="Quit",
        command=close,
        fg="white",
        bg="red")
    leave.pack()
    # spacer
    dummy(bottomframe)

    # ==== Key Binding ====

    # Consider binding these these to buttons
    # Pressing <Return> runs the out() function
    root.bind('<Return>', out)
    # Use <Escape> to quit using close() method
    root.bind('<Escape>', close)

# For exiting the application
def close(*event):
    """
    close: procedure for closing app

    Close the app,

    1. show popup,
    2. change browser contents,
    3. destroy root


    :rtype: bool

    :param event: Optional

    :type event: event

    """

    root.after(40000, lambda: root.destroy())
    # Thank you for playing messagebox
    pop("Thank you", "Thank you for learning with us!")
    # open page in default browser
    webbrowser.open(
        'http://23eyes.org/fair',
        new=0,
        autoraise=False)
    # Destroy the Window for the application
    root.destroy()

# function to create vertical space
def dummy(parent):
    """
    This function makes an empty label. It's used several times to add vertical space between widgets in the root window.

    :param parent: the variable can be set to root, midFrame, or bottomframe

    :type parent: str

    :rtype: bool

    """
    # make space out of a single <space> character in the target part of the interface.
    spacer = ttk.Label(parent, text=" ")
    # label parent window; label content defined as 2x whitespace character
    spacer.pack()


# === Main Function ===


def main(args=None):
    """
    Main Function

    Main function wraps all the code. It's the main routine; the functions within main() are subroutines.

    parameters: none
    """

    # Python Conventions: Run the program - do not take any modifiers
    if args is None:
        args = sys.argv[1:]

    # Global Variables: not restricted to specific scope
    global fontFace, correct, ques, count, title, fontFace, browserName, correct, ques, count, entry, further, root, browserName, question, answer

    # === Lists ===

    # ==== List of Questions =====

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
        "She said \"radical\" simply means \"grasping by the roots.\"\n\n"]

    # ==== Answers List ====

    # Answers match the above questions (in same order) come afterwards.
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


    # **These are the first actions to happen**

    # === Variables Get Set ===

    # Number of questions answered correctly
    correct = 0
    # current question number (starts count at 0)
    ques = 0
    # total number of answers (and questions)
    count = len(answer)
    # Root window title
    title = "Protest & Resist (Power to the People!)"
    # Sets the font used for the questions/prompts
    fontFace = 'arial 14 bold'
    # creates the root window of the interface
    root = tk.Tk()
    # sets geometry for root window
    root.geometry('{}x{}'.format(600, 700))
    # name at top of dialog
    windowtitle = root.wm_title(title)
    # call the widgets function to populate the window
    widgets()
    # Create splash dialog (message box); calls the pop function
    splash = pop("Welcome", "Protest & Resist (Power to the People!)\n\nEnter your answers in the form of a question (like Jeopardy) -- Capitalization, spelling, and punctuation count. At the top of the game, you'll see possible answers. Press 'OK' to submit an answer; press 'Quit' to end the game.\n")
    # Keep the game at the forefront of the desktop
    root.attributes('-topmost', True)
    # loops everything until told to quit (run out of questions or press
    # <Escape> or click quit
    root.mainloop()



# Python idiom - everything runs within the main() function
# to learn more,
# visit <http://ibiblio.org/g2swap/byteofpython/read/module-name.html>
if __name__ == "__main__":
    main()
