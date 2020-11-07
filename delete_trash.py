import os
import shutil

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__pycache__')
shutil.rmtree(path)
