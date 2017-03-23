#! /bin/bash -ex
# Builds with Nuitka a WIndows distribution (exe) of the code
nuitka --standalone ./main/jeopardy-tk.py --output-dir ./nuitka/
