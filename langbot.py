from router_solver import *
from word.word import *
from scanner.scanner import *
from language.language import *
from training.training import *

vocabulary = Scanner.create_vocabulary("data/lesson1.csv")
language = Language(vocabulary, "Deutsch")
Training(language).play()
