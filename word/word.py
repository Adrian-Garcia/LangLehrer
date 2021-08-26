from router_solver import *


class Word(object):
    def __init__(
        self, word, gender=None, translation=None, word_type=None, declination=None
    ):
        self.word = word
        self.gender = gender
        self.translation = translation
        self.word_type = word_type
        self.declination = declination

    def __print_declination(self):
        pass

    def print(self):
        if self.gender:
            print("{} {}".format(self.gender, self.word))
        else:
            print(self.word)

        if self.translation:
            print("  traducción:", self.translation)

        if self.word_type:
            print("  tipo:", word.word_type)

        if self.declination:
            self.__print_declination()

        print()
