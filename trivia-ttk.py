from Tkinter import *
import Tkinter as tk
import ttk
import sys



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
title = "Jeopardy: Black History Month Edition"

#troubleshooting
#print(count)


#creates empty root window
root = Tk()



# this is only working for the first question. Maybe that is fine.
whois = StringVar(root, value='Who is...?')

# geometry for root window
root.geometry('{}x{}'.format(1024, 500))




#name at top of dialog
windowtitle = root.wm_title(title)

# grip for resizing window "root"
grippy = ttk.Sizegrip(root)
grippy.pack()

#grippy.pack()

#this should be cleared after the first question
rules = ttk.Label(root,text='Welcome. Please remember to enter your answers in the form of a question. Capitalization, punctualion, and spelling matter.\n\n')
rules = rules.pack()

#question as label
font = 'arial 16 bold'
label = ttk.Label(root,text = question[ques],wraplength=500, justify=LEFT, font=font)
label.pack()

# Does not Work Properly: Should be there for each question

entry = ttk.Entry(root, width=50, textvariable=whois)
entry.pack()

score = ttk.Label(root, text = "Score: 0/0")
score.pack()

# Progressbar
further = ttk.Progressbar(mode="determinate",orient="horizontal", maximum=count,value=0,variable=ques)
further.pack()


def out():

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
                sys.exit(0)


    #else:
    #    #entry.delete(0, END)
    #    #label.config(text = "Correct: " + str(correct) + "out of " + str(ques))

    #    sys.exit()





def stop():

    sys.exit()


# Buttons call functions

# Submit Button calls Quiz and is default
submit = ttk.Button(root,text = "OK",command = out)
root.bind('<Return>', (lambda e, button=submit: submit.invoke()))
submit.pack()

# quitit button calls stop function
quitit = ttk.Button(root,text = "Quit",command = stop)
root.bind('<Escape>', (lambda e, button=quitit: quitit.invoke()))
quitit.pack()



root.mainloop()
