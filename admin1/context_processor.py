from .forms import *
from bookapp.forms import *
from bookapp.models import *

def genre_links(request):
    genre = Category.objects.all()
    return {'genre':genre}

def book_search(request):
    search_form = BookSearchForm()
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}
