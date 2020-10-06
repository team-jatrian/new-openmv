from shutil import copy
import glob
import os

files = glob.glob('*.txt')
directory = os.getcwd()
for file in files: 
    copy(fr'{directory}\{file}', r'C:\Users\sinan\OneDrive\Coding\Python\uploader\test')