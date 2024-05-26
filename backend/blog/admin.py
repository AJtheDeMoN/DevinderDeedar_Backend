from django.contrib import admin
from .models import Article
from .models import Story
from .models import Prose

admin.site.register(Article)
admin.site.register(Story)
admin.site.register(Prose)
