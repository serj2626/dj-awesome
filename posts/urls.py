from django.urls import path
from .views import (
    PostCreateView, HomeView, PostDelete,
    PostEditView, PostDetailView, CategoryView
)


urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<pk>/', PostDelete.as_view(), name='post_delete'),
    path('post/edit/<pk>/', PostEditView.as_view(), name='post_edit'),
    path('post/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
]
