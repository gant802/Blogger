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
    


