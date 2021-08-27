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
            translation = current_word.translation

            if current_word.gender:
                word_and_gender = "{} {}".format(current_word.gender, current_word.word)
                self.translated_words_in_language[translation] = word_and_gender
                self.language_words_translations[word_and_gender] = translation

            else:
                self.translated_words_in_language[translation] = current_word.word
                self.translated_words_in_language[current_word.word] = translation

            self.translated_words.append(translation)
            self.language_words.append(word_and_gender)

    def get_random_word(self):
        words = self.vocabulary.get_words().values()
        return random.choice(list(words))
