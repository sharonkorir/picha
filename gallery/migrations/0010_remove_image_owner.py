# Generated by Django 4.0.3 on 2022-03-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_alter_image_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
    ]
