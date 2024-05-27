# lib/helpers.py
from models.author import Author 
from models.post import Post


#def helper_1():
#    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def add_author():
    author = input("Author name: ")
    Author.create(author)

def write_post():
    from cli import create_menu
    author_ids = [f"{object.id}: {object.name}" for object in Author.get_all()]
    if len(author_ids) > 0:
        author_id = int(input(f"Enter an author id from this list {author_ids} "))
        while author_id not in [object.id for object in Author.get_all()]:
            print("name not in list")
            author_id = int(input(f"Enter an author id from this list {author_ids} "))
        title = input("Enter a title: ")
    else:
        print("no authors found. must add an author first.")
        create_menu()

    
    category = input(f"Enter a category from list of categories {Post.categories}: ")
    while category not in Post.categories:
        print("invalid category")
        category = input(f"Enter a category from list of categories {Post.categories}: ")
    content = input("Post content: ")
    Post.create(title, content, category, author_id)
    print("Post created successfully!")
    

def view_authors():
    authors = Author.get_all()
    for author in authors:
        print(f"{author.name} id:{author.id}")

def find_author_by_id():
    id_ = input("Enter the author's id: ")
    author = Author.find_by_id(id_)
    print(f"--Author: {author.name}--") if author else print(f'Author {id_} not found')

def find_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    print(f"--Author: {author.name}--") if author else print(
        f'Author {name} not found')

def view_authors_posts():
    author_name = input("Enter the author's name: ")
    author_object = Author.find_by_name(author_name)
    if author_object:
        try:
            posts = author_object.find_all_posts()
            for post in posts:
                print(f"Title: {post.title}, Category: {post.category} || {post.content}")
        except Exception as exc:
            print("Error finding posts: ", exc)
    else :
        print(f"Author named {author_name} not found")



def view_all_posts():
    posts = Post.get_all()
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"Title: {post.title}, Category: {post.category}, Author: {author.name}|| {post.content}\n\n")
    else :
        print("No posts found")

def view_posts_by_category():
    category = input("Enter the category: ")
    posts = Post.find_by_category(category)
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"Title: {post.title}, Author: {author.name}|| {post.content}\n\n")