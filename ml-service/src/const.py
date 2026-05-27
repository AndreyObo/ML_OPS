import os

current_dir = os.path.dirname(os.path.abspath(__file__))

LOG_URL = os.environ.get('LOG_URL', None)

MODELS_DIR = os.path.join(current_dir, 'models')
DATA_DIR =  os.path.join(current_dir, 'data')