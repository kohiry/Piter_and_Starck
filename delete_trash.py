import os
import shutil

try:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__pycache__')
    shutil.rmtree(path)
except Exception:
    print()
#os.system("TASKKILL /F /IM "+"game.db")
#path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'game.db')
#os.remove(path)
