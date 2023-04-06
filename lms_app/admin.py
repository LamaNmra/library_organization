from django.contrib import admin
from django.forms import *
from django.db.models import *
#from tinymce.widgets import TinyMCE
from .models import *
# Register your models here.

#admin.site.register(Model, ModelAdmin)
admin.site.register(Book)
admin.site.register(Categury)
#admin.site.register(BookForms)