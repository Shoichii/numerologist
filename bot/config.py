import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ADM_IDS = int(os.environ.get('ADM_IDS'))