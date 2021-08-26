from router_solver import *
from word.word import *
from scanner.scanner import *
from language.language import *

vocabulary = Scanner.create_vocabulary("data/lesson1.csv")
language = Language(vocabulary, "Deutsch")
