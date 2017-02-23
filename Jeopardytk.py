#!/usr/bin/python

import tkinter
top = tkinter.Jeopardy()
# Code to add widgets will go here...

import Tkinter
import tkMessageBox

top = Tkinter.Jeopardy()
def hello():
   tkMessageBox.showinfo("result", "Correct")

B1 = Tkinter.Button(top, text = "submit", command = hello)
B1.pack()



E1.pack(side = RIGHT)
def main():

    correct = 0
    question = 0
    count = len(Answers)
  
    message = "Phrase your answer as a question. Remember: spelling, punctuation, and capitalization matter."

    while question < int(count):
        ask = inputbox(d,Questions[question])


        if ask == Answers[question]:
            correct = correct + 1
            infobox(d,"Answer Correct")
            question = question + 1
            tkmessagebox(, str(correct) + "/" + str(question) + " correct.")

        else:
            tkmessagebox.showinfo("result", "Answer Incorrect")
            question = question + 1

    exit()

top.mainloop()




Questions =[
"She is a civil-rights activist that argued for the abolition of prisons. \n\n",

"He is the civil-rights leader who described potentially radical action in support of civil rights progress as \"marvelous new militancy\".\n\n",

"She is a civil-rights activist that argued \"We have nothing to lose but our chains.\"\n\n",

"He believed \"a riot is the voice of the unheard.\"\n\n"

"He was the lawyer to Malcom X \n\n"
 
"Who believed that freedom is only earned every generation?\n\n"
 
"Who said that, “\Hate is too great a burden to bear. It injures the hater more than it injures the hated.\”\n\n"
    
"Who believed that \“all Americans who believe in freedom” should “oppose bigotry and prejudice based on sexual orientation\”\n\n"

"She said “It is our duty to fight for our freedom. It is our duty to win. We must love each other and support each other. We have nothing to lose but our chains.”

"According to him, “The revolution has always been in the hands of the young. The young inherit the revolution.” 

"She said “No one is going to give you the education you need to overthrow them”.,

"She said  “it is our duty to fight for our freedom. It is our duty to win.”,

"He said “You don't fight racism with racism, the best way to fight racism is with solidarity.”,

"Who said “You can jail a revolutionary, but you can not jail the revolution.”, 

"She said “I don't believe you can stand for freedom  for one group of people and deny it to others.” ,
 
"She makes clear that “the political core of any movement for freedom in the society has to have the political imperative to protect free speech.” 

"He wrote “the secret of life is to have no fear; it's the only way to function”.
 
"She said “ I will not have my life narrowed down. I will not bow down to somebody else’s whim or to someone else’s ignorance.” 

"He said “If you see something that is not right, not fair, not just, you have a moral obligation to do something about it.”

"She said,  “being oppressed [dominated] means the absence of choices.”

"She said, “I want there to be a place in the world where people can engage in one another’s differences in a way that is redemptive, full of hope and possibility. Not this ‘In order to love you, I must make you something else’. That’s what domination is all about, that in order to be close to you, I must possess you, remake and recast you.” 

"He said, “The civil rights movement was based on faith. Many of us who were participants in this movement saw our involvement as an extension of our faith. We saw ourselves doing the work of the Almighty. Segregation and racial discrimination were not in keeping with our faith, so we had to do something.”
 
"He said, “Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.”
 
"She said that, “hate is too great a burden to bear. It injures the hater more than it injures the hated.”
 
"S/he believed that “all Americans who believe in freedom” should “oppose bigotry and prejudice based on sexual orientation.”
 
"She said “this is the 21st century; we need to redefine revolution.”
 
"He said “Don’t give up, Don't give out, Don't give in.” 
 
"She said “Feminism is for everybody.”
 
"She said “radical” simply means “grasping by the roots.”
 
]

Answers = [
"Who is Dr. Angela Davis?",

"Who is Dr. Martin Luther King, Jr.?",

"Who is Assata Shakur?",

"Who is Dr. Martin Luther King, Jr.?",

"Who is Percy Sutton?",
    
"Who is Coretta Scott King?",

"Who is Coretta Scott King?",
    
"Who is Coretta Scott King?"
 
"Who is Assata Shakur?

"Who is Huey P. Newton? 
 
"Who is Assata Shakur?

"Who is Assata Shakur?

"Who is Bobby Seale?
 
"Who is Bobby Seale?
 
"Who is Coretta Scott King?
 
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
 
"Who is Dr. Angela Davis?",
