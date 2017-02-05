# -*- coding: utf-8 -*-


def listDivide(numbers, divide=2):
    num = 0
    for i in numbers:
        if i % divide == 0:
            num += 1
    return num

def testListDivide():
    try:
        listDivide([1, 2, 3, 4, 5])
        listDivide([1, 2, 3, 4, 5], 1)
        listDivide([])
        listDivide([30, 54, 63, 98, 100], divide=10)
        listDivide([2, 4, 6, 8, 10])
    except (RuntimeError, TypeError, NameError, ValueError):
        raise ListDivideException(self)


class ListDivideException(object):

    def __init__(self):
        print 'an error occurred'

if __name__ == '__main__':
    testListDivide()
