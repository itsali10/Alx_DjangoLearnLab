from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

books = Book.objects.all()
book.title="Nineteen Eighty-Four"
book.save()
book.delete()
Book.objects.all()