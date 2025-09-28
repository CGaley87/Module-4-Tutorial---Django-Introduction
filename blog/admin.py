#Curtis Galey
#admin.py
#Contents copy and pasted from site to create admin login.

from django.contrib import admin
from .models import Post

admin.site.register(Post)


