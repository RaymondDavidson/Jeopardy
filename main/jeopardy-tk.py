#!/usr/bin/env python
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

"""
Summary:

This is a program written in Python.


"""

from Tkinter import *
import Tkinter as tk
import tkMessageBox
import sys
import ttk as ttk
import shelve


# people who worked on this project (in list format)
credits = ["Ocho262", "FlamboyantPapayas", "ghoulmann", "Sidhant", "CY", "JF", "RC", "EB", "MS"]

"""
These are the prompts in the game that
players anwer (in the form of a question

"""


question = ["(1) She is a civil-rights activist that argued for the abolition of prisons.\n\n",

"(2) He is the civil-rights leader who described potentially radical action in support of civil rights progress as \"marvelous new militancy\".\n\n",

"(3) She is a civil-rights activist that argued \"We have nothing to lose but our chains.\"\n\n",

"(4) He believed \"a riot is the voice of the unheard.\"\n\n",

"(5) He was the lawyer to Malcom X. \n\n",

"(6) He believed that freedom is only earned every generation.\n\n",

"(7) This activist said that, \"Hate is too great a burden to bear. It injures the hater more than it injures the hated.\"\n\n",

"(8) Who believed that \"all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation.\"\n\n",

"(9) She said \"It is our duty to fight for our freedom. It is our duty to win. We must love each other and support each other. We have nothing to lose but our chains.\"\n\n",

"(10) According to him, \"The revolution has always been in the hands of the young. The young inherit the revolution.\"\n\n",

"(11) She said \"No one is going to give you the education you need to overthrow them.\"\n\n",

"(12) She said  \"It is our duty to fight for our freedom. It is our duty to win.\"\n\n",

"(13) He said \"You don't fight racism with racism, the best way to fight racism is with solidarity.\"\n\n",

"(14) He said \"You can jail a revolutionary, but you can not jail the revolution.\"\n\n",

"(15) She said \"I don't believe you can stand for freedom  for one group of people and deny it to others.\"\n\n",

"(16) She makes clear that \"the political core of any movement for freedom in the society has to have the political imperative to protect free speech.\"\n\n",

"(17) He wrote \"the secret of life is to have no fear; it's the only way to function.\"\n\n",

"(18) She said \"I will not have my life narrowed down. I will not bow down to somebody else's whim or to someone else's ignorance.\"\n\n",

"(19) He said \"If you see something that is not right, not fair, not just, you have a moral obligation to do something about it.\"\n\n",

"(20) She said, \"being oppressed means the absence of choices.\"\n\n",

"(21) She said, \"I want there to be a place in the world where people can engage in one another's differences in a way that is redemptive, full of hope and possibility. Not this \'In order to love you, I must make you something else\'. That's what domination is all about, that in order to be close to you, I must possess you, remake and recast you.\"\n\n",

"(22) He said, \"The civil rights movement was based on faith. Many of us who were participants in this movement saw our involvement as an extension of our faith. We saw ourselves doing the work of the Almighty. Segregation and racial discrimination were not in keeping with our faith, so we had to do something.\"\n\n",

"(23) He said, 'Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.\"\n\n",

"(24) She said that, \"hate is too great a burden to bear. It injures the hater more than it injures the hated.\"\n\n",

"(25) She believed that \"all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation.\"\n\n",

"(26) She said \"this is the 21st century; we need to redefine revolution.\"\n\n",

"(27) He said \"Don't give up, Don't give out, Don't give in.\"\n\n",

"(28) She said \"Feminism is for everybody.\"\n\n",

"(29) She said \"radical\" simply means \"grasping by the roots.\"\n\n"]

"""
:type :list[str]
"""

answer = ["Who is Dr. Angela Davis?",

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

#troubleshooting
#print("quiz")

#### Set Some Vars ####
correct = 0
ques = 0
count = len(answer)
title = "Protest & Resist (Power to the People!)"

def pop(title, string):
    tkMessageBox.showinfo(title, string)

def out(event):

    global correct, ques, count, entry, further


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
            ques = ques + 1
            entry.delete(0, END)
            if ques < count:
                label.config(text = question[ques])
                score.config(text=("Score: " + str(correct) + "/" + str(ques)))
            else:
                stop()




def close(event):
    shelf = shelve.open('scores.dat') # here you will save the score variable
    shelf['score'] = str(correct)      # thats all, now it is saved on disk.
    shelf.close() # closes the db file with scores
    pop("Thank you", "Please play again!")
    sys.exit()



def stop():
    shelf = shelve.open('./scores.dat') # here you will save the score variable
    shelf['score'] = str(correct) # thats all, now it is saved on disk.
    shelf.close()
    pop("Thank you", "Please play again!")
    sys.exit()

#creates empty root window
root = tk.Tk()

# Create 1st pop up message box
pop("Welcome", "Protest & Resist (Power to the People)")
pop("How to Play", "Enter your answers in the form of a question (like Jeopardy) -- Capitalization, spelling, and punctuation count. At the top of the game, you'll see possible answers. Press 'OK' to submit an answer; press 'Quit' to end the game.")


# bind escape to root window action - Throws and error
#root.bind("<Escape>", stop)

# this is only working for the first question. Maybe that is fine.
whois = StringVar(root, value='Who is...?')

# geometry for root window
root.geometry('{}x{}'.format(600, 600))


#frame experiment
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )



#name at top of dialog
windowtitle = root.wm_title(title)




#######REMOVE########
# grip for resizing window "root"
#grippy = ttk.Sizegrip(bottomframe)
#grippy.pack(side = RIGHT, anchor="se")

#grippy.pack()




people = ttk.Label(root,wraplength=500, foreground="red", text="Dr. Angela Davis, Dr. Martin Luther King, Jr., Assata Shakur, bell hooks, Stokely Carmichael, Bobby Seale, Percy Sutton, Coretta Scott King, Huey P. Newton, Rep. John Lewis\n\n")
people.pack()

#question as label
font = 'arial 16 bold'
label = ttk.Label(root,text = question[ques],wraplength=300, font=font)
label.pack()



entry = ttk.Entry(root, width=40, textvariable=whois)
entry.pack()


dummy = tk.Label(root, text=" ")
dummy.pack()


score = ttk.Label(bottomframe, text = "Score: 0/0", font=font)
score.pack()


# Submit button to continue game
submit = tk.Button(bottomframe,text = "OK",command = out, fg="white", bg="green")
submit.pack()

# If it's the last question, it makes no sense to continue: in this case, close program (record score)

root.bind('<Return>', out)







def dummy():
    """
    Create a 2-space \"empty\" label to act as a spacer since we're not using grid
    """

    dummy = ttk.Label(bottomframe, text=" ")
    dummy.pack()











#horizontal spacers
dummy()
dummy()
dummy()

# quit button
# quitit button calls stop function
leave = tk.Button(bottomframe,text = "Quit",command = stop, fg="white", bg="red")
root.bind('<Escape>', close)

leave.pack()


dummy()




#make and pack progressbar: (no color)

further = ttk.Progressbar(bottomframe, mode="determinate",orient="horizontal", maximum=count, variable=ques, length=300, value=0)
further.pack()

#make label
pb = ttk.Label(bottomframe, text="Progress")
pb.pack()






root.mainloop()
s = shelve.open('score.txt') # here you will save the score variable
d[str(correct)] = score           # thats all, now it is saved on disk.
