# Generated by Django 3.0.3 on 2020-03-03 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20200303_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]