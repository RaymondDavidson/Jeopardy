#! /bin/bash -ex
sudo apt update
sudo apt install nuitka
# Builds with Nuitka a WIndows distribution (exe) of the code
nuitka --standalone ./main/jeopardy-tk.py --output-dir ./nuitka/
echo "Windows package is in $(pwd)/nuitka/"
