from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from corsheaders.signals import check_request_enabled

from .models import Article
from .models import Story
from .models import Prose

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = {
        'id': article.id,
        'title': article.title_punjabi,
        'content': article.content.replace("`", "<p>"),
        'author': article.author,
        'year': article.year,
    }
    return JsonResponse(data)

def article_list(request):
    articles = Article.objects.all()
    article_list = [{'id': article.id, 'title_punjabi': article.title_punjabi,'title_english':article.title_english,'book_punjabi':article.book_punjabi,'book_english':article.book_english,'year':article.year} for article in articles]
    return JsonResponse({'articles': article_list})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    data = {
        'id': story.id,
        'title': story.title_punjabi,
        'content': story.content.replace("`", "<p>"),
        'author': story.author,
        'year': story.year,
    }
    return JsonResponse(data)

def story_list(request):
    stories = Story.objects.all()
    story_list = [{'id': story.id, 'title_punjabi': story.title_punjabi,'title_english':story.title_english,'year':story.year} for story in stories]
    return JsonResponse({'stories': story_list})

def prose_list(request):
    proses = Prose.objects.all()
    prose_list = [{'id': prose.id, 'content':prose.content} for prose in proses]
    return JsonResponse({'proses': prose_list})

def activator(request):
    return JsonResponse({'ok': 'ok'})

