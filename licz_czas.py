from time import time


def licz_czas(funkcja, *args):
    start = time()
    funkcja(*args)
    end = time()
    return end - start
