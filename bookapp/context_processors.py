from .models import Category
from .forms import BookSearchForm, AuthorSearchForm

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def book_search(request):
    search_form = BookSearchForm
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}

def author_search(request):
    author_form = AuthorSearchForm
    if request.method == 'POST':
        author_form = AuthorSearchForm(request.POST)
        if author_form.is_valid():
            author_form.save()
    return{'author_form':author_form}