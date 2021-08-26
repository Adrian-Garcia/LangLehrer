from router_solver import *
from language.language import *
import os
from time import sleep


class Training(object):
    def __init__(self, language):
        self.language = language
        
    def play(self):
        print("Hello")
        user_option = "play"

        while user_option != None:
            Training.__print_menu()
            user_option = input("Opción: ")

            if user_option in ["A", "a", "1"]:
                pass

            elif user_option in ["B", "b", "2"]:
                pass

            elif user_option in ["Z", "z", "0"]:
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
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def __original_to_translated():
        pass

    def __translated_to_original():
        pass