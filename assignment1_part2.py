# -*- coding: utf-8 -*-


class Book(object):

    def __init__(self, author='', title=''):
        self.author = author
        self.title = title


    def display(self):
        line = '{}, written by {}'.format(self.title, self.author)
        return line

obj1 = Book(author='John Steinbeck', title='Of Mice and Men')
print obj1.display()

obj2 = Book(author='Harper Lee', title='To Kill a Mockingbird')
print obj2.display()