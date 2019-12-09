from make_cbz import make_cbz
from tkinter import filedialog
from tkinter import *
from os import listdir

root = Tk()
root.withdraw()
directory = filedialog.askdirectory()

for x in listdir(directory):
    make_cbz(directory + '/' + x)
