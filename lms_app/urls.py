#from django import path
from turtle import update
from django.urls import path
from . import views
urlpatterns =[
   path('',views.index,name='index'),
   path('book',views.book,name='book'), 
   path('update/<int:id>',views.update,name='update'),
   path('delet/<int:id>',views.delet,name='delet'),

]