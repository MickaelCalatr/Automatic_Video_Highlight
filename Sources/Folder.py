import os
import shutil
import glob

def create(name):
    if not os.path.exists(name):
        os.makedirs(name)

def delete(name):
    if os.path.exists(name):
        shutil.rmtree(name)

def remove(name):
    if os.path.exists(name):
        os.remove(name)
