import dialog
import time
import sys

Questions =[
"She is a civil-rights activist that argued for the abolition of prisons. \n\n",

"He is the civil-rights leader who described potentially radical action in support of civil rights progress as \"marvelous new militancy\".\n\n",

"She is a civil-rights activist that argued \"We have nothing to lose but our chains.\"\n\n",

"He believed \"a riot is the voice of the unheard.\"\n\n"

"He was the lawyer to Malcom X \n\n"
 
"Who believed that freedom is only earned every generation?\n\n"
 
"Who said that, “\Hate is too great a burden to bear. It injures the hater more than it injures the hated.\”\n\n"
    
"Who believed that \“all Americans who believe in freedom” should “oppose bigotry and prejudice based on sexual orientation\”\n\n"
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
