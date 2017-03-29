def askGoogle(string):
    """In case of wrong answer, show correct 'person' from google search.

    Turns correct answer into a google ask, and then opens a browser tab to the google search results.

    Relies on default browser of the system to improve compatibility.

    Args
    ~~~~

    :param string (str): The question to look up (from the list)



    Returns
    -------

    :return bool: True for success. False otherwise.


    """

    ask = string
    ask = ask.replace(" ", "+")
    www = "https://www.google.com/#q=" + ask + "&*"
    platform = os.name
    if platform == "posix":
        try:
            webbrowser.open(www, new=0, autoraise=False)
        except:
            print "We're sorry; we couldn't show the answer with a browser."
    else:
        try:
            webbrowser.open(www, new=0, autoraise=False)
        except:
            print "Couldn't raise a browser."


def pop(title, string):
    """
    We used three pop-up message boxes in the course of development.
    We don't repeat ourselves, so we just called this function each
    time we need a messagebox to appear.

    parameters
    ----------

    title (str): Title of the dialog
    string (str): message of the messagebox

    """
    msg = tkMessageBox
    msg = msg.showinfo(title, string)


# function for continuing (on correct or incorrect answer)
def out(*event):
    """
    Output to the main window. Changes after each answer is submitted, until there are no questions left to answer.

    parameters
    ----------

    event (event): Optional. How to work with <Enter> key stroke or Submit button being pressed.

    """
    global correct, ques, count, entry, further, root, browserName

    # bring cursor to the input field
    entry.focus()
    # change progress bar
    further["value"] = ques
    # process input
    ans = entry.get()
    # conditional: if still questions left to answer, do the things that follow.
    if ques < count:
        entry.focus()
        further["value"] = ques
        further.pack()
        # conditional: if answer is correct, increase score, change question.
        if ans == answer[ques]:
            correct = correct + 1
            ques = ques + 1
            entry.delete(0, END)
            label.config(text = question[ques])
            score.config(text=("Score: " + str(correct) + "/" + str(ques)))
        # if not correct answer, do what follows.
        else:
            askGoogle(answer[ques])
            #askGoogle(answer[ques], browserName)
            root.after(0500, lambda:root.focus_force())
            entry.focus()
            ques = ques + 1
            entry.delete(0, END)
            entry.focus()

    # if there are questions left, go to next question
    if ques < count:
        label.config(text = question[ques])
        score.config(text=("Score: " + str(correct) + "/" + str(ques)))
    # if no more questions, close program.
    else:
        # call the close function with no parameters
        close()

def widgets():
    """
    Function for adding all the widgets to the graphical user interface. Also sets up two frames for the lower 2/3 of frames.

    Parameters:
    None

    """
    global fontFace, further, entry, label, score

    #frame inside window to control bottom element layout
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    # midFrame for entry
    midFrame = Frame(root)
    midFrame.pack(side=BOTTOM)

    #### root widgets ####

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
    root.after(40000, lambda: root.destroy())
    pop("Thank you", "Thank you for learning with us!")
    webbrowser.open('https://github.com/ghoulmann/Jeopardy', new=0, autoraise=False)
    root.destroy()

def dummy(parent):
    """ This function makes an empty label. It's used several times to add vertical space between widgets in the root window.

    Parameters:

    parent (variable): the variable can be set to root, midFrame, or bottomframe
    """

    spacer = ttk.Label(parent, text = " ")
    spacer.pack()
