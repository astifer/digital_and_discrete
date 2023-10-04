import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GROUP_KEY = os.environ.get("GROUP_KEY")
KEYBOARD_KEY = os.environ.get("KEYBOARD_KEY")
