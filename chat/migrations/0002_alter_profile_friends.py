# Generated by Django 5.0.2 on 2024-02-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friends', to='chat.friend'),
        ),
    ]