import dialog
import sys

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
                  "exit this demo?"
        else:
            msg = "You pressed ESC in the last dialog box. Do you want to " \
                  "exit this demo?"
        # "No" or "ESC" will bring the user back to the demo.
        # DIALOG_ERROR is propagated as an exception and caught in main().
        # So we only need to handle OK here.
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
        return 0
    else:
        return 1                        # code is d.DIALOG_OK


def box(d,message):
    d.msgbox(message)



def main():
    """This demo shows the main features of the pythondialog Dialog class.
    """
    ok = "Welcome to Jeopardy: Liberation Edition.\n Please remember to answer in the form of a question.\n Spelling, capitalization, and punctuation matter."
    d = dialog.Dialog(dialog="dialog")

    d.add_persistent_args(["--backtitle", "Arise!"])

    try:
        box(d,ok)
    except dialog.error, exc_instance:
        sys.stderr.write("Error:\n\n%s\n" % exc_instance.complete_message())
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__": main()
