# Generated by Django 3.1.5 on 2021-01-15 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210115_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='published_date',
        ),
    ]