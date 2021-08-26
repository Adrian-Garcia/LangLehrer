from router_solver import *


class Word(object):
    def __init__(self, word, gender=None, word_type=None, declination=None):
        self.word = word
        self.gender = gender
        self.word_type = word_type
        self.declination = declination

    def hello(self):
        print("Hello")
