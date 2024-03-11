from django.urls import path
from .views import ProfileView, ProfileEditView, ProfileDeleteView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<int:pk>/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),

]
