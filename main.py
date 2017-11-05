#!/usr/bin/env python3
"""
Module Docstring
"""
import TwoSATClassifier

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

def print_result(problem):
    filename = "2sat{}.txt".format(problem)
    myfile = open(filename, "r")
    vertices = int(myfile.readline())
    clauses = vertices
    two_sat_classifier = TwoSATClassifier.TwoSATClassifier(vertices, clauses)
    for line in myfile:
        values = line.split()
        two_sat_classifier.add_clause(int(values[0]), int(values[1]))
    myfile.close()    
    print("{}, {}".format(problem, two_sat_classifier.is_satisfiable()))


def main():
    """ Main entry point of the app """
    for i in range(6):
        print_result(i+1)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
