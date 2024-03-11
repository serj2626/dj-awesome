# Generated by Django 5.0.2 on 2024-03-11 09:18

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default/profile.png', null=True, upload_to=users.models.get_path_for_avatar, verbose_name='аватар'),
        ),
    ]