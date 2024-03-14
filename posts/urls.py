from django.urls import path
from .views import (
    PostCreateView, HomeView, PostDelete,
    PostEditView, PostDetailView, CategoryView, 
    comment_delete, reply_sent, reply_delete
)


urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<pk>/', PostDelete.as_view(), name='post_delete'),
    path('post/edit/<pk>/', PostEditView.as_view(), name='post_edit'),
    path('post/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('comment/<pk>/delete/', comment_delete, name='comment_delete'),
    path('reply-sent/<pk>/', reply_sent, name='reply_sent'),
    path('reply-delete/<pk>/', reply_delete, name='reply_delete'),
]
