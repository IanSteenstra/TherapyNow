# Generated by Django 3.0.7 on 2020-08-12 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageflag',
            old_name='receiver',
            new_name='flagged_user',
        ),
    ]
