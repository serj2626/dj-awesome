from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid
from .service import get_path_for_icon
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('название', max_length=500)
    artist = models.CharField('имя исполнителя', max_length=500, null=True)
    url = models.URLField('ссылка фликер', max_length=500, null=True)
    image = models.URLField('ссылка на картинку', max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='posts', null=True)
    body = models.TextField('текст поста', blank=True)
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField('дата создания', auto_now_add=True)
    updated = models.DateTimeField('дата обновления', auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created']

    def __str__(self):
        return self.title

    property

    # def default_name(self):
    #     if not self.author:
    #         return {'name': 'Аноним',
    #                 'username': 'user'}


class Tag(models.Model):
    name = models.CharField('название', max_length=50, unique=True)
    icon = models.FileField(
        'иконка', upload_to=get_path_for_icon, null=True, blank=True)
    order = models.IntegerField('порядок', null=True)
    slug = models.SlugField('слаг', max_length=50, unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ['order']

    def __str__(self):
        return self.name
