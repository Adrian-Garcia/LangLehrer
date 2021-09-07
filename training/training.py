from router_solver import *
from termcolor import colored
from enum import Enum
from language.language import *
import os
from time import sleep


class Games(Enum):
    ORIGINAL_TO_TRANSLATED = 1
    TRANSLATED_TO_ORIGINAL = 2
    DIE_DER_DAS = 3


class Training(object):
    OPTIONS = 3
    GENDERS = ["die", "der", "das"]

    def __init__(self, language):
        self.language = language

    def play(self):
        user_option = "play"

        while user_option != None:
            Training.__print_menu()
            user_option = input("Opción: ")

            if user_option in ["A", "a", "1"]:
                self.__question_manager(Games.ORIGINAL_TO_TRANSLATED)

            elif user_option in ["B", "b", "2"]:
                self.__question_manager(Games.TRANSLATED_TO_ORIGINAL)

            elif user_option in ["C", "c", "3"]:
                self.__question_manager(Games.DIE_DER_DAS)

            elif user_option in ["Z", "z", "0", "-1"]:
                print("¡Nos vemos luego!")
                user_option = None

            else:
                _ = input("Opcion no válida, oprima cualquier tecla para continuar")
                user_option = "play"

    def __print_menu():
        Training.__screen_clear()
        print("¿Qué deseas entrenar?")
        print("A) Palabras de alemán a español")
        print("B) Palabras de español a alemán")
        print("C) Die, der, das")
        print("Z) Salir")

    def __screen_clear():
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    def __question_manager(self, option):
        questions = []
        options = []

        for i in range(self.language.vocabulary.get_size()):
            quest, opt = self.__get_question_and_options()

            if quest not in questions:
                questions.append(quest)
                options.append(opt)

        while len(questions):
            question = questions.pop(0)
            opt = options.pop(0)

            if option == Games.ORIGINAL_TO_TRANSLATED:
                grade = self.__original_to_translated(question, opt)

            elif option == Games.TRANSLATED_TO_ORIGINAL:
                grade = self.__translated_to_original(question, opt)

            elif option == Games.DIE_DER_DAS:
                grade = self.__die_der_das(question)

            if not grade:
                questions.append(question)
                options.append(opt)

    def __get_question_and_options(self):
        question = self.language.get_random_word()
        options = [question]

        while len(options) != Training.OPTIONS:
            possible_response = self.language.get_random_word()
            if possible_response not in options:
                options.append(possible_response)

        random.shuffle(options)

        return [question, options]

    def __original_to_translated(self, question=None, options=None):
        if question == None or options == None:
            question, options = self.__get_question_and_options()

        Training.__screen_clear()
        print(
            'Traducción de "{} {}:"\n'.format(question.gender, question.word)
            if question.gender
            else 'Traducción de "{}":\n'.format(question.word)
        )
        Training.__show_options(list(map(lambda opt: opt.translation, options)))
        user_response = int(input("\nRespuesta: ")) - 1
        grade = options[user_response] == question
        Training.__rate(grade)

        return grade

    def __translated_to_original(self, question=None, options=None):
        if question == None or options == None:
            question, options = self.__get_question_and_options()

        Training.__screen_clear()
        print('Traducción de "{}":\n'.format(question.translation))
        Training.__show_options(
            list(
                map(
                    lambda option: "{} {}".format(option.gender, option.word)
                    if option.gender
                    else option.word,
                    options,
                )
            )
        )
        user_response = int(input("\nRespuesta: ")) - 1
        grade = options[user_response] == question
        Training.__rate(grade)

        return grade

    def __die_der_das(self, question=None):
        if question == None:
            question = self.language.get_random_word()

        Training.__screen_clear()
        print('Genero de "{}":\n'.format(question.word))
        Training.__show_options(Training.GENDERS)
        user_response = int(input("\nRespuesta: ")) - 1
        grade = Training.GENDERS[user_response] == question.gender
        Training.__rate(grade)

        return grade

    def __rate(grade):
        if grade:
            text = "\nRespuesta correcta! Oprime cualquier tecla para continuar\n"
            color = "green"
        else:
            text = "\nRespuesta incorrecta! Oprime cualquier tecla para continuar\n"
            color = "red"

        input(colored(text, color))

    def __show_options(options):
        for i in range(Training.OPTIONS):
            print("Opción {}: {}".format(i + 1, options[i]))
