# Generated by Django 3.1.2 on 2020-10-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]