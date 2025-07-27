from relationship_app import models


def get_books_by_author(author_name):
    author=models.Author.objects.get(name=author_name)
    return author.objects.filter(author=author)
    
def list_all_books_in_library(library_name):

    library = models.Library.objects.get(name=library_name)
    return library.books.all()
    
def get_librarian_of_library(library_name):
    librarian = models.Librarian.objects.get(library=library_name)
    return librarian.librarian.name 