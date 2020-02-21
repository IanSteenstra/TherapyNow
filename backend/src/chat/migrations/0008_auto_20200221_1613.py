# Generated by Django 3.0.2 on 2020-02-21 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_profile_friends'),
        ('chat', '0007_auto_20200220_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='contact',
        ),
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Profile.Profile'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='chats', to='Profile.Profile'),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
