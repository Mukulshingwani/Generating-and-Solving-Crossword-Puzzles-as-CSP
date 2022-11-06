from csp_crossword import CspCrossword
import numpy as np
import csv
import time

from utils import print_title


def main():
    lemmas = get_lemmas()
    # print(lemmas)
    start_forward_check_algorithm(4,5, lemmas)


def get_lemmas():
    file1 = open('words_file.txt', 'r')
    Lines = file1.readlines()
    words = []
    for line in Lines:
        # print(line.rstrip())
        words.append(str(line.strip()))
    return np.array(words)


def start_backtracking_algorithm(size_min, size_max, lemmas):
    for size_y in range(size_min, size_max + 1):
        for size_x in range(size_min, size_max + 1):
            print_title('CSP CROSSWORD: start')
            print_title('CSP CROSSWORD: init square with size ' + str(size_y) + 'x' + str(size_x))
            csp_crossword = CspCrossword(size_y, size_x)
            print_title('CSP CROSSWORD: fill square with words (backward algorithm)')
            start_time = time.time()
            csp_crossword.backward_assign_words(lemmas)
            end_time = time.time()
            print('Time elapsed: ', end_time - start_time)
            print('Result')
            csp_crossword.plot()
            csp_crossword.print_result()
            print_title('CSP CROSSWORD: end')


def start_forward_check_algorithm(size_min, size_max, lemmas):
    for size_y in range(size_min, size_max + 1):
        for size_x in range(size_min, size_max + 1):
            print_title('CSP CROSSWORD: start')
            print_title('CSP CROSSWORD: init square with size ' + str(size_y) + 'x' + str(size_x))
            csp_crossword = CspCrossword(size_y, size_x)
            print_title('CSP CROSSWORD: fill square with words (forward check algorithm)')
            square_possible_opts, square_possible_vals = csp_crossword.init_foreward_check_board(lemmas, size_y, size_x)
            start_time = time.time()
            csp_crossword.forward_assign_words(square_possible_opts, square_possible_vals)
            end_time = time.time()
            print('Time elapsed: ', end_time - start_time)
            print('Result')
            csp_crossword.plot()
            csp_crossword.print_result()
            print_title('CSP CROSSWORD: end')


main()

