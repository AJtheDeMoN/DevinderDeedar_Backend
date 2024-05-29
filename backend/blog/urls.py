from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Make sure the view function name matches
    path('story/', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),  # Make sure the view function name matches
    path('prose/', views.prose_list, name='prose_list'),
    path('activator/', views.activator, name='activator'),
]
