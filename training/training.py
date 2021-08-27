from router_solver import *
from language.language import *
import os
from time import sleep


class Training(object):
    OPTIONS = 3

    def __init__(self, language):
        self.language = language

    def play(self):
        print("Hello")
        user_option = "play"

        while user_option != None:
            Training.__print_menu()
            user_option = input("Opción: ")

            if user_option in ["A", "a", "1"]:
                self.__original_to_translated()

            elif user_option in ["B", "b", "2"]:
                self.__translated_to_original()

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
        print("Z) Salir")

    def __screen_clear():
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    def __get_question_and_options(self):
        question = self.language.get_random_word()
        options = [question]

        while len(options) != Training.OPTIONS:
            possible_response = self.language.get_random_word()
            if possible_response not in options:
                options.append(possible_response)

        random.shuffle(options)

        return [question, options]

    def __original_to_translated(self):
        question, options = self.__get_question_and_options()
        Training.__screen_clear()

        if question.gender:
            print('Traducción de "{} {}:"\n'.format(question.gender, question.word))

        else:
            print('Traducción de "{}":\n'.format(question.word))

        for i in range(Training.OPTIONS):
            print("Opcion {}: {}".format(i, options[i].translation))

        user_response = int(input("\nRespuesta: "))

        if options[user_response] == question:
            _ = input("\nRespuesta correcta! Oprime cualquier tecla para continuar\n")
        else:
            _ = input("\nRespuesta incorrecta! Oprime cualquier tecla para continuar\n")

    def __translated_to_original(self):
        question, options = self.__get_question_and_options()
        Training.__screen_clear()

        print('Traducción de "{}":\n'.format(question.translation))

        for i in range(Training.OPTIONS):
            option = options[i]

            if option.gender:
                print("Opcion {}: {} {}".format(i, option.gender, option.word))
            else:
                print("Opcion {}: {}".format(i, option.word))

        user_response = int(input("\nRespuesta: "))

        if options[user_response] == question:
            _ = input("\nRespuesta correcta! Oprime cualquier tecla para continuar\n")
        else:
            _ = input("\nRespuesta incorrecta! Oprime cualquier tecla para continuar\n")
