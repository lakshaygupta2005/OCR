import sys
import os

# Add your project directory to the Python path
project_home = '/home/LakshayGupta1234/my_OCR_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your app from app.py
from app import app as application