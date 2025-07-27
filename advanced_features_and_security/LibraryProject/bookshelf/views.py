from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from advanced_features_and_security.LibraryProject.bookshelf.models import Book

from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm




content_type = ContentType.objects.get_for_model(Book)
editors_group, created = Group.objects.get_or_create(name='Editors')
edit_permission = Permission.objects.get(codename='can_edit', content_type=content_type)
create_permission = Permission.objects.get(codename='can_create', content_type=content_type)
editors_group.permissions.add(edit_permission, create_permission)

@permission_required('bookshelf.can_edit', raise_exception=True)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

