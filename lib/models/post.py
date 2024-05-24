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
    
    #? only accepts type str and 1 to 20 characters
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 0 < len(new_title) <= 20:
            self._title = new_title

    @property 
    def content(self):
        return self._content
    
    #? only accepts type str and at least 1 charachter
    @content.setter
    def content(self, new_content):
        if isinstance(new_content, str) and len(new_content) > 0:
            self._content = new_content

    @property
    def category(self):
        return self._category
    
    #? only accepts if category is in categories
    @category.setter
    def category(self, new_category):
        if new_category in Post.categories:
            self._category = new_category

    
    #? Creates posts table if it doesn't already exist
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

    #? Deletes the posts table 
    @classmethod
    def drop_table(cls):
        """ Drop the table to persist the attributes of Post instances """
        sql = "DROP TABLE IF EXISTS posts"

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, content, category and author_id values of the current Post object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO posts (title, content, category, author_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.content, self.category, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Post instance."""
        sql = """
            UPDATE posts
            SET title = ?, content = ?, category = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.content,
                             self.category, self.author_id, self.id))
        CONN.commit()