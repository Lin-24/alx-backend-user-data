#!/usr/bin/env python3
""" This module initializes the views for the API.
It imports and registers all the blueprints for different endpoints of the API
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
