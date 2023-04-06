
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from turtle import title
from django import forms
from .models import Book, Categury
 
class categuryForm(forms.ModelForm):
    class Meta:
        model=Categury
        fields=['name',]
        Widget={'name': forms.TextInput(attrs={'class':"forms-control"})}

class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['titel',
                 'author',
                 'photo_book',
                 'photo_aythor',
                 'pages',
                 'price',
                 'status',
                 'categury',
                 'reyal_price_day',
                 'retal_period',
                 'total_rental',
                 ]
        widgets ={
                 'titel':forms.TextInput(attrs={'class':'forms-control'}),
                 'author': forms.TextInput(attrs={'class':"forms-control"}),
                 'price': forms.NumberInput(attrs={'class':"forms-control"}),
                 'photo_book': forms.FileInput(attrs={'class':"forms-control"}),
                 'photo_aythor': forms.FileInput(attrs={'class':"forms-control"}),
                 'pages': forms.NumberInput(attrs={'class':"forms-control"}),
                 'reyal_price_day': forms.NumberInput(attrs={'class':"forms-control", 'id':'rental_price'}),
                 'retal_period': forms.NumberInput(attrs={'class':"forms-control", 'id':'period_rental'}),
                 'total_rental': forms.NumberInput(attrs={'class':"forms-control", 'id':'total_rental'}),
                 'status': forms.TextInput(attrs={'class':"forms-control"}),
                 'categury': forms.TextInput(attrs={'class':"forms-control"}),}