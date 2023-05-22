from app import http_app
import os
from controller import *

if __name__ == '__main__':
    http_app.run(host=os.environ.get('MY_WEB_HOST', '0.0.0.0'), port=os.environ.get('MY_WEB_PORT', '5001'))