from models.__init__ import CURSOR, CONN

class Post():
    all = {}

    def __init__(self, title, content, author_id, id = None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, author_id={self.author_id})"