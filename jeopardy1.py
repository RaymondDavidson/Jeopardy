import dialog
import time
import sys

Questions =[
"(1) She is a civil-rights activist that argued for the abolition of prisons. \n\n",

"(2) He is the civil-rights leader who described potentially radical action in support of civil rights progress as \"marvelous new militancy\".\n\n",

"(3) She is a civil-rights activist that argued \"We have nothing to lose but our chains.\"\n\n",

"(4) He believed \'a riot is the voice of the unheard.\'\n\n"

"(5) He was the lawyer to Malcom X \n\n"
 
"(6) Who believed that freedom is only earned every generation?\n\n"
 
"(7) Who said that, '\Hate is too great a burden to bear. It injures the hater more than it injures the hated.\'\n\n"
    
"(8) Who believed that \'all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation\'\n\n"

"(9) She said 'It is our duty to fight for our freedom. It is our duty to win. We must love each other and support each other. We have nothing to lose but our chains.\'\n\n"

"(10) According to him, 'The revolution has always been in the hands of the young. The young inherit the revolution.\'\n\n" 

"(11) She said 'No one is going to give you the education you need to overthrow them.\'\n\n",

"(12) She said  'it is our duty to fight for our freedom. It is our duty to win.\'\n\n",

"(13) He said 'You don't fight racism with racism, the best way to fight racism is with solidarity.\'\n\n",

"(14) Who said 'You can jail a revolutionary, but you can not jail the revolution.\'\n\n", 

"(15) She said 'I don't believe you can stand for freedom  for one group of people and deny it to others.\'\n\n",
 
"(16) She makes clear that 'the political core of any movement for freedom in the society has to have the political imperative to protect free speech.\'\n\n" 

"(17) He wrote 'the secret of life is to have no fear; it's the only way to function.\'\n\n"
 
"(18) She said 'I will not have my life narrowed down. I will not bow down to somebody else’s whim or to someone else’s ignorance.\'\n\n"

"(19) He said 'If you see something that is not right, not fair, not just, you have a moral obligation to do something about it.\'\n\n"

"(20) She said, 'being oppressed [dominated] means the absence of choices.\'\n\"

"(21) She said, "I want there to be a place in the world where people can engage in one another’s differences in a way that is redemptive, full of hope and possibility. Not this ‘In order to love you, I must make you something else’. That’s what domination is all about, that in order to be close to you, I must possess you, remake and recast you.\"\n\n" 

"(22) He said, 'The civil rights movement was based on faith. Many of us who were participants in this movement saw our involvement as an extension of our faith. We saw ourselves doing the work of the Almighty. Segregation and racial discrimination were not in keeping with our faith, so we had to do something.\'\n\n"
 
"(23) He said, 'Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.\'\n\n"
 
"(24) She said that, 'hate is too great a burden to bear. It injures the hater more than it injures the hated.\'\n\n"
 
"(25) She believed that 'all Americans who believe in freedom should oppose bigotry and prejudice based on sexual orientation.\'\n\n"
 
"(26) She said 'this is the 21st century; we need to redefine revolution.\'\n\n"
 
"(27) He said 'Don’t give up, Don't give out, Don't give in.\'\n\n" 
 
"(28) She said 'Feminism is for everybody.\'\n\n"
 
"(29) She said “radical” simply means “grasping by the roots.”\n\n"
 
]

Answers = [
"(1) Who is Dr. Angela Davis?",

"(2) Who is Dr. Martin Luther King, Jr.?",

"(3) Who is Assata Shakur?",

"(4) Who is Dr. Martin Luther King, Jr.?",

"(5) Who is Percy Sutton?",
    
"(6) Who is Coretta Scott King?",

"(7) Who is Coretta Scott King?",
    
"(8) Who is Coretta Scott King?",
 
"(9) Who is Assata Shakur?",

"(10) Who is Huey P. Newton?",
 
"(11) Who is Assata Shakur?",

"(12) Who is Assata Shakur?",

"(13) Who is Bobby Seale?",
 
"(14) Who is Bobby Seale?",
 
"(15) Who is Coretta Scott King?",
 
"(16) Who is bell hooks?",
 
"(17) Who is Stokely Carmichael?",
 
"(18) Who is bell hooks?",
 
"(19) Who is Rep. John Lewis?",
 
"(20) Who is bell hooks?",
 
"(21) Who is bell hooks?",

"(22) Who is Rep. John Lewis?",
 
"(23) Who is Dr. Martin Luther King, Jr.?",

"(24) Who is Coretta Scott King?",
 
"(25) Who is Coretta Scott King?",
 
"(26) Who is Assata Shakur?",
 
"(27) Who is Rep. John Lewis?",
 
"(28) Who is bell hooks?",
 
"(29) Who is Dr. Angela Davis?",
 
]

def handle_exit_code(d, code):
    """Sample function showing how to interpret the dialog exit codes.
    This function is not used after every call to dialog in this demo
    for two reasons:
       1. For some boxes, unfortunately, dialog returns the code for
          ERROR when the user presses ESC (instead of the one chosen
          for ESC). As these boxes only have an OK button, and an
          exception is raised and correctly handled here in case of
          real dialog errors, there is no point in testing the dialog
          exit status (it can't be CANCEL as there is no CANCEL
          button; it can't be ESC as unfortunately, the dialog makes
          it appear as an error; it can't be ERROR as this is handled
          in dialog.py to raise an exception; therefore, it *is* OK).
       2. To not clutter simple code with things that are
          demonstrated elsewhere.
    """
    # d is supposed to be a Dialog instance
    if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
        if code == d.DIALOG_CANCEL:
            msg = "You chose cancel in the last dialog box. Do you want to " \
                  "exit Jeopardy?"
        else:
            msg = "You pressed ESC in the last dialog box. Do you want to " \
                  "exit Jeopardy?"
        # "No" or "ESC" will bring the user back to the game.
        # DIALOG_ERROR is propagated as an exception and caught in main().
        # So we only need to handle OK here.
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
        return 0
    else:
        return 1                        # code is d.DIALOG_OK

def infobox(d,msg):
    d.infobox(msg)
    time.sleep(2)

def inputbox(d,question):
    while 1:
        (code,response) = d.inputbox(question, init="Who is...?")
        if handle_exit_code(d,code):
            break

    return response

def main():

    correct = 0
    question = 0
    count = len(Answers)


    message = "Phrase your answer as a question. Remember: spelling, punctuation, and capitalization matter."

    d = dialog.Dialog(dialog="dialog")
    d.add_persistent_args(["--backtitle", "Civil Rights Jeopardy"])
    infobox(d,message)

    while question < int(count):
        ask = inputbox(d,Questions[question])

        if ask == Answers[question]:
            correct = correct + 1
            infobox(d,"Answer Correct")
            question = question + 1
            infobox(d, str(correct) + "/" + str(question) + " correct.")

        else:
            infobox(d, "Answer Incorrect")
            question = question + 1

    exit()



main()
