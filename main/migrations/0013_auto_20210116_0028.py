# Generated by Django 3.1.5 on 2021-01-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210116_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='insta',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]