# Python Dialog

## Prepare

Install gdebi package:

`sudo apt update`

`sudo apt install gdebi wget curl`

## Get the Package

Go to Downloads folder:

`cd ~/Downloads`

Download the .deb package for pythondialog from TurnKey Linux:

`wget http://archive.turnkeylinux.org/debian/pool/jessie/main/p/python-dialog/python-dialog_2.7-1turnkey%2b9%2bg97403e1_amd64.deb`

Download python-support to satisfy dependency:

`wget http://launchpadlibrarian.net/109052632/python-support_1.0.15_all.deb`

## Install Packages

Make sure you are in the ~/Downloads directory.

Then:

`sudo gdebi python-support_1.0.15_all.deb`

Then:

`sudo gdebi python-dialog_2.7-1turnkey%2b9%2bg97403e1_amd64.deb`

Assuming everything went smoothly, you can now make use of dialog in a Python script with `import dialog`.
