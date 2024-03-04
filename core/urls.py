from django.contrib import admin
from django.urls import path, include
from posts.views import home_view, PostCreateView,HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('post/create/',PostCreateView.as_view(), name='post_create'),
]
