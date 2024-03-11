from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


def get_path_for_avatar(instance, filename):
    return f'avatars/{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        'аватар', upload_to=get_path_for_avatar, null=True, blank=True, default='default/profile.png')
    name = models.CharField('имя', max_length=50)
    email = models.EmailField('почта', max_length=60, unique=True, null=True)
    location = models.CharField('местоположение', max_length=200, blank=True)
    bio = models.TextField('биография', null=True, blank=True)
    created = models.DateTimeField('дата создания', auto_now_add=True)


    class Meta:
        verbose_name = _("Профиль")
        verbose_name_plural = _("Профили")


    def __str__(self):
        return f'Профиль {self.user}'