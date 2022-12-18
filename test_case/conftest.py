import os

import pytest

from utils.read import base_data
from api.user_api import login

def get_data():
    return base_data.read_data()



