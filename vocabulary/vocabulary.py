from router_solver import *
from word.word import *


class Vocabulary(object):
    def __init__(self, words):
        self.__words = words

    def add_word(self, word_name, word):
        self.__words[word_name] = word

    def get_words(self):
        return self.__words

    def print_words(self):
        for word in self.__words:
            self.__words[word].print()

    def get_size(self):
        return len(self.__words)
