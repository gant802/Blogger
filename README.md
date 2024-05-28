# Blogger CLI+ORM Project

## Create authors and posts to be persisted to a relational database backend, all within the CLI!

This a a group project that was created by Don Jacody and Grant Cummings to showcase our skills we have aquired learning how to interact with a database. The project uses Python along with SQL commands to interact with a sqlite3 database. As a user you will be able to do the following:

* Initially choose between a set of options to redirect you to 4 different types of menus that have to do with create, read, update and deleting authors or posts
* Create authors to be intialized with a name and favorite category
* Create posts to be initialized with a title, content, category and author id
* Find authors by name or id from database
* Find posts by title or id from database
* View all authors
* View all posts
* View all posts by a specific author 
* View all posts by a specific category
* View number of posts by an author
* Update authors and posts
* Delete authors and posts
* Exit the program

## How to install and use this application in your local computer

1. Fork and clone the repo to a repository within your GitHub.
2. Open the project in your code editor of choice (ours is VS Code)
3. In your terminal within the the project's folder run "$ pipenv install" to install all dependencies for the project
4. Run "$ pipenv shell" to create a shell environment to use the program
5. Run "$ python lib/cli.py" to use the program within your terminal


## Final note
This is a backend only project and would work much better if there was a frontend when it comes to the amount of posts that can be generated. This project is a representation of the skills we have when interacting with the database of a program. 