# Generated by Django 4.0.3 on 2022-03-29 08:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_remove_image_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
