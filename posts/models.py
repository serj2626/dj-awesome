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


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField('текст', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Комментарий к посту {self.post} от {self.author}'
    
    def save(self, *args, **kwargs):
        if not self.author:
            self.author = 'Пользователь удален'
        return super().save(*args, **kwargs)


class Reply(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies")
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    # likes = models.ManyToManyField(User, related_name='likedreplies', through='LikedReply')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['created']