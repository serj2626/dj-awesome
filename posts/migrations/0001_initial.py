# Generated by Django 5.0.2 on 2024-03-04 00:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500, verbose_name='название')),
                ('image', models.URLField(max_length=500, verbose_name='ссылка картинки')),
                ('body', models.TextField(verbose_name='текст поста')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
