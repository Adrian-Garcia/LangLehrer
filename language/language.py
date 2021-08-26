from router_solver import *
from vocabulary.vocabulary import *
import random

class Language(object):
    def __init__(self, vocabulary, name=None):
        self.vocabulary = vocabulary
        self.name = name
        self.translated_words = []
        self.language_words = []
        self.translated_words_in_language = dict()
        self.language_words_translations = dict()
        self.__start()

    def __start(self):
        words = self.vocabulary.get_words()

        for word in words:
            current_word = words[word]

            if current_word.gender:
                self.translated_words_in_language[
                    current_word.translation
                ] = "{} {}".format(current_word.gender, current_word.word)
                self.language_words_translations[
                    "{} {}".format(current_word.gender, current_word.word)
                ] = current_word.translation
            else:
                self.translated_words_in_language[
                    current_word.translation
                ] = current_word.word
                self.translated_words_in_language[
                    current_word.word
                ] = current_word.translation

            self.translated_words.append(current_word.translation)
            self.language_words.append(
                "{} {}".format(current_word.gender, current_word.word)
            )

    def get_random_word(self):
        words = self.vocabulary.get_words().values()
        return random.choice(words)