from router_solver import *
from vocabulary.vocabulary import *
import csv


class Scanner(object):
    def create_vocabulary(file_name, file_type=None):
        vocabulary = Vocabulary(dict())

        with open(file_name, newline="") as csv_file:
            vocabulary_list = list(csv.reader(csv_file, delimiter=" ", quotechar="|"))
            dimensions = len(vocabulary_list.pop(0)[0].split(","))

            if dimensions == 2:
                Scanner.__scann_two_dimensions(vocabulary, vocabulary_list)

            elif dimensions == 3:
                Scanner.__scann_three_dimensions(vocabulary, vocabulary_list)

        return vocabulary

    def __scann_two_dimensions(vocabulary, vocabulary_list):
        for row in vocabulary_list:
            word_values = row[0].split(",")
            word = Word(word_values[1], word_values[0])
            vocabulary.add_word(word_values[1], word)

    def __scann_three_dimensions(vocabulary, vocabulary_list):
        for row in vocabulary_list:
            word_values = row[0].split(",")

            print(word_values)

            word = Word(word_values[1], word_values[0], word_values[2])
            vocabulary.add_word(word_values[1], word)
