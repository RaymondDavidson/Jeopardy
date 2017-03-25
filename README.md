# Jeopardy

civil rights jeopardy - repo for HS students.

# Requires

* python 2.7
* Tkinter
* shelve

# jeopardy-tk.py

* Game mechanics work
* quit button works without throwing error

## To Do

* [] order the code again - conflicts have made everything out of sequence (but still working)
* [] Elaborate on setup.py
* [] make and attach an icon for the window manager
* [] add debian package instructions to README.md
* [] strike nuitka
* [] make it work portably on windows
* [] docstrings for functions

# Python-dialog.py

learning game With tui dialog wrapper from TurnKey GNU/Linux

# Build

## Windows
*   nuitka --standalone ./main/jeopardy-tk.py (useless so far)

## Otherwise

Requires stdeb

```
cd main/
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/<folder with project and version> #determined in setup.py
dpkg-buildpackage -rfakeroot -uc -us
```

----

Shoulda been a javascript project.
