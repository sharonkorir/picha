# Generated by Django 4.0.3 on 2022-03-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='editor',
            new_name='owner',
        ),
    ]
