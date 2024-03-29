# Generated by Django 5.0.2 on 2024-03-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='artist',
            field=models.CharField(max_length=500, null=True, verbose_name='имя исполнителя'),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=500, null=True, verbose_name='ссылка фликер'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=500, verbose_name='ссылка на картинку'),
        ),
    ]
