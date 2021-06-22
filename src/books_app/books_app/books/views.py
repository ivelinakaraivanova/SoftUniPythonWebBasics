from django.shortcuts import render, redirect

from books_app.books.forms import BookForm, AuthorForm, StateFilterForm
from books_app.books.models import Book


# def show_create_form(request, form):
#     context = {
#         'form': form,
#     }
#     return render(request, 'create.html', context)
#
#
# def show_update_form(request, form):
#     context = {
#         'form': form,
#     }
#     return render(request, 'edit.html', context)

#1st variant
# def show_book_form(request, form, template_name):
#     context = {
#         'form': form,
#     }
#     return render(request, template_name, context)

#2nd variant
def show_book_form(request, book_form, author_form, template_name):
    context = {
        'book_form': book_form,
        'author_form': author_form,
    }
    return render(request, template_name, context)

# 1st variant
# def save_book_from_form(request, form, template_name):
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#
#     return show_book_form(request, form, template_name)

# 2nd variant
def save_book_from_form(request, book_form, author_form, template_name):
    if book_form.is_valid() and author_form.is_valid():
        author = author_form.save()
        book = book_form.save(commit=False)  # za da ne izgurmi zaradi ForeignKey; vrushta instance bez da ya zapazva v bazata
        book.author = author
        book.save()
        return redirect('index')

    return show_book_form(request, book_form, author_form, template_name)


# def index(request):
#     context = {
#         'books': Book.objects.all()
#     }
#
#     return render(request, 'index.html', context)


def index(request):
    filter_form = StateFilterForm(request.GET)
    filter_form.is_valid()
    state = filter_form.cleaned_data['state']
    books = []
    if state == 'all':
        books = Book.objects.all()

    context = {
        'filter_form': filter_form,
        'books': books
    }

    return render(request, 'index.html', context)


# 1st variant
# def create_book(request):
#     if request.method == 'GET':
#         form = BookForm()
#         return show_book_form(request, form, 'create.html')
#     else:
#         form = BookForm(request.POST)
#
#                 # if form.is_valid():
#                 #     form.save()
#                 #     return redirect('index')
#                 # return show_book_form(request, form, 'create.html')
#
#         return save_book_from_form(request, form, 'create.html')

#2nd variant
def create_book(request):
    if request.method == 'GET':
        book_form = BookForm()
        author_form = AuthorForm()
        return show_book_form(request, book_form, author_form, 'create.html')
    else:
        book_form = BookForm(request.POST)
        author_form = AuthorForm(request.POST)

                # if form.is_valid():
                #     form.save()
                #     return redirect('index')
                # return show_book_form(request, form, 'create.html')

        return save_book_from_form(request, book_form, author_form, 'create.html')


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "GET":
        form = BookForm(
            initial=book.__dict__,  # instance=book - the same in this case
        )
        return show_book_form(request, form, 'edit.html')
    else:
        form = BookForm(
            request.POST,
            instance=book,
        )

        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        #
        # return show_book_form(request, form, 'edit.html')

        return save_book_from_form(request, form, 'edit.html')
