# Generated by Django 4.0.3 on 2022-03-27 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poster',
            new_name='Owner',
        ),
    ]