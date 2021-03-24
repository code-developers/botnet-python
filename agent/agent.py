#!/usr/bin/env/python3
# coding: utf-8

#imports
import requests
import time
import os
import subprocess
import platform
import shutil
import sys
import traceback
import threading
import uuid
import StringIO
import zipfile
import tempfile
import socket
import getpass
if os.name == 'nt':
    from PIL import ImageGrab
else:
    import pyscreenshot as ImageGrab

import config

def threaded(func):
    def wrapper(*_args, **kwargs):
        t = threading.Thread(target=func, args=_args)
        t.start()
        return
    return wrapper
