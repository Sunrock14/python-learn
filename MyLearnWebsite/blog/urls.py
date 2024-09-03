from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("index", views.home),
    path("blog", views.blog),
    path("blog/<int:id>", views.blog_detail),
]
