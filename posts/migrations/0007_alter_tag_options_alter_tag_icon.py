# Generated by Django 5.0.2 on 2024-03-10 19:48

import posts.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_tag_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='icon',
            field=models.ImageField(null=True, upload_to=posts.service.get_path_for_icon, verbose_name='иконка'),
        ),
    ]