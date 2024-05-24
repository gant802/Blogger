from models.__init__ import CURSOR, CONN

class Author:

    def __init__ (self, name, author_id=None):
        self.name = name
        self.author_id = author_id

    def __repr__(self):
        return f'<Author name={self.name}'
    

    @property
    def name(self):
        return self._name
    
    #name must be str and between 1 and 15 characters inclusive
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 15:
            self._name = new_name