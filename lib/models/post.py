from models.__init__ import CURSOR, CONN

class Post():
    all = {}
    categories = ['sports', 'news', 'pop', 'nature']

    def __init__(self, title, content, category, author_id, id = None):
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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Post instances """
        sql = """
            CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            category TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table to persist the attributes of Post instances """
        sql = "DROP TABLE IF EXISTS posts"

        CURSOR.execute(sql)
        CONN.commit()
