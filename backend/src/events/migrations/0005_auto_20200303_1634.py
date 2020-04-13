# Generated by Django 3.0.3 on 2020-03-03 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200228_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Scheduling', 'verbose_name_plural': 'Scheduling'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Ending Time', verbose_name='Ending Time'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Starting Time', verbose_name='Starting Time'),
        ),
    ]