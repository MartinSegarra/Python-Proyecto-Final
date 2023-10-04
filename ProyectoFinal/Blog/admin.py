from django.contrib import admin
from Blog.models import Redactor, Moderador, Comentador

# Register your models here.

admin.site.register(Redactor)

admin.site.register(Comentador)

admin.site.register(Moderador)
