"""
import sys
import os
from pprint import pprint as pp
proj_path = os.getcwd()
sys.path.append(proj_path)
pp(sys.path)
"""

from sandbox_web import app

app.run(host="0.0.0.0", debug=True)
