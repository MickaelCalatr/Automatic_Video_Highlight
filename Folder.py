import os
import shutil
import glob

class Folder:
    def create(self, name):
        if not os.path.exists(name):
            os.makedirs(name)

    def delete(self, name):
        if os.path.exists(name):
            shutil.rmtree(name)
            
    def remove(self, name):
        if os.path.exists(name):
            os.remove(name)
