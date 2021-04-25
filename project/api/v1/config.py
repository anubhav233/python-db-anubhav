import os


class Config(object):
    HELLO_KEY = os.getenv("HELLO_KEY", "AVCDAFASF")
