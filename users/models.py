from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

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
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
