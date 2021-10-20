# - The `os` module provide assess to 
# - The `shutil` module provides access to methods that allow 

# Useful method in shutil
import os, shutil

# create a ddirectory
cur_dir = os.getcwd()
# prints the current working directory
print(cur_dir)          
path = './test'
os.mkdir(path)
os.chdir(path)
# we should now be in the new directory
print(os.getcwd())  