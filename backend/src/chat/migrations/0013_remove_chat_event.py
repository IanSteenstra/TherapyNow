# Generated by Django 3.0.4 on 2020-03-31 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_remove_chat_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='event',
        ),
    ]