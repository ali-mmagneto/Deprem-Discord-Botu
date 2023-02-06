import re
import os
from os import environ

BOT_TOKEN = environ.get("BOT_TOKEN", "")
API_ID = int(environ.get("API_ID", 1234))
API_HASH = environ.get("API_HASH", "")
