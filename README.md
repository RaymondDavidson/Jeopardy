# Jeopardy

civil rights jeopardy - repo for HS students' project.

# Requires

* python 2.7
* python-tkinter


# jeopardy_quiz/jeopardy_quiz.py

* Game mechanics work
* quit button works without throwing error
* launches browser window in event of wrong answer

## To Do

* [ ] Make and incorporate wm icon
* [ ] try again with qt
* [ ] Build submodules
* [ ] autogenerate documentation
* [ ] recreate in javascript, cython

# Python-dialog.py

learning game With tui dialog wrapper from TurnKey GNU/Linux

# Build

## Build sdist

`python setup.py sdist`

use pip install to install.

## Build Debian

*On a debian-based machine*

### Requires stdeb

```
cd main/
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/<folder with project and version> #determined in setup.py
dpkg-buildpackage -rfakeroot -uc -us
```

### From Source packages

```
py2dsc <name-of-package-version.tar.gz>
cd deb_dist/<name-of-package-version>
dpkg-buildpackage -rfakerooot -uc -us
cd ..
sudo dpkg -i python-<name-of-package-version_all.deb>
----

Shoulda been a javascript project.
