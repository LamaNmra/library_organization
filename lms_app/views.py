from curses import tigetflag
import re
from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import bookForm,categuryForm
# Create your views here.
def index(request):
   if request.method=='POST':
       add_book=bookForm(request.POST, request.FILES)
       if add_book.is_valid():
        add_book.save()
       add_categery=categuryForm(request.POST)
       if add_categery.is_valid():
           add_categery.save()

   contex={'book':Book.objects.all(),
            'categury':Categury.objects.all(),
            'form':bookForm(),
            'formcat':categuryForm(),
            'allbook':Book.objects.filter(active=True).count(),
            'booksold':Book.objects.filter(status='sold').count(),
            'bookrental':Book.objects.filter(status='rental').count(),
            'bookavailable':Book.objects.filter(status='available').count(),
     }
   return render(request,'pages/index.html',contex)

def book(request):
    search=Book.objects.all()
    titel=None
    if 'search_name' in request.GET:
        titel =request.GET['search_name']
        if titel:
            search =search.filter(titel__icontains=titel)

    contex={'book':search,
            'category':Categury.objects.all(),
            'form':bookForm(),
            'formcat':categuryForm(),
     }
    return render(request,'pages/book.html',contex)

def delet(request,id):
    book_delet=get_object_or_404(Book,id=id) 
    if request.method=='POST':
         book_delet.delete()
         return redirect('/')
    return render(request,'pages/delet.html')

def update(request,id): 
         book_id= Book.objects.get(id=id) 
         if request.method=='POST':
          book_save=bookForm(request.POST,request.FILES,instance=book_id)
          if book_save.is_valid():
              book_save.save()
              return redirect('/')
         else :
          book_save=bookForm(instance=book_id)  
         contex={'form':book_save}      
         return render(request,'pages/update.html',contex)