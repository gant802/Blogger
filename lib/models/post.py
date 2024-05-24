from models.__init__ import CURSOR, CONN

class Post():
    all = {}
    categories = ['sports', 'news', 'pop', 'nature']

    def __init__(self, title, content, category, author_id=None, id = None):
        self.id = id
        self.title = title
        self.content = content
        self.category = category
        self.author_id = author_id

    def __repr__(self):
        return f"<Post title={self.title}, content={self.content}, category={self.category}, id={self.id}, author_id={self.author_id}>"
    
    @property
    def title(self):
        return  self._title
    
    #only accepts type str and 1 to 20 characters
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 0 < len(new_title) <= 20:
            self._title = new_title

    
