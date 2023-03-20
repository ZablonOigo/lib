from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'library/index.html', context)


# def detail(request,pk):
#     num_books=get_object_or_404(Book,pk=pk)
#     context={'num_books':num_books}
#     return render(request,'library/book_list.html', context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list' 
    queryset = Book.objects.all() 
    template_name = 'library/book_list.html'  


# class BookDetailView(generic.DetailView):
#     model = Book
#     def book_detail_view(request, pk):
#           book = get_object_or_404(Book, pk=pk)
#           return render(request, 'library/book_detail.html', context={'book': book})

def detail(request,id):
    book=get_object_or_404(Book, pk=id)
    context={'book':book}
    return render(request, 'library/book_detail.html',context)