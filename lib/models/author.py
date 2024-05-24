from models.__init__ import CURSOR, CONN

class Author:

    def __init__ (self, name, author_id=None):
        self.name = name
        self.author_id = author_id

    def __repr__(self):
        return f'<Author name={self.name}'