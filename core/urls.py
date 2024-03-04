from django.contrib import admin
from django.urls import path, include
from posts.views import PostCreateView, HomeView, post_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<pk>/', post_delete_view, name='post_delete'),
]
