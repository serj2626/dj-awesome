from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from posts.views import (
    PostCreateView, HomeView, PostDelete,
    PostEditView, PostDetailView, CategoryView,
)

handler404 = 'posts.views.page_not_found'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('posts.urls')),
    path('profile/', include('users.urls')),
#     path('', HomeView.as_view(), name='home'),
#     path('post/create/', PostCreateView.as_view(), name='post_create'),
#     path('post/delete/<pk>/', PostDelete.as_view(), name='post_delete'),
#     path('post/edit/<pk>/', PostEditView.as_view(), name='post_edit'),
#     path('post/<pk>/', PostDetailView.as_view(), name='post_detail'),
#     path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
