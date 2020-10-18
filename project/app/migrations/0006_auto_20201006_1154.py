# Generated by Django 3.1.2 on 2020-10-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200914_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='audio_link',
            field=models.TextField(blank=True, default='', verbose_name='Audio Link'),
        ),
        migrations.AddField(
            model_name='item',
            name='audio_path',
            field=models.TextField(blank=True, default='', verbose_name='Audio Filepath'),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[(0, 'Die-YT'), (1, 'Gov-YT'), (3, 'Live-YT'), (4, 'Bad Link'), (5, 'Unchecked')], default=5, verbose_name='Trạng thái'),
        ),
    ]
