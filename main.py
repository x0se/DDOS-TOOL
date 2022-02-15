#coded by x0se

from importlib import import_module
from sys import path

path.insert(1, "./Raven-Storm/")
main = import_module("Raven-Storm.main")

main.run()
