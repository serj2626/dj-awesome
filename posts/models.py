from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('название', max_length=500)
    artist = models.CharField('имя исполнителя', max_length=500, null=True)
    url = models.URLField('ссылка фликер', max_length=500, null=True)
    image = models.URLField('ссылка на картинку', max_length=500)
    body = models.TextField('текст поста', blank=True)
    created = models.DateTimeField('дата создания', auto_now_add=True)
    updated = models.DateTimeField('дата обновления', auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})
