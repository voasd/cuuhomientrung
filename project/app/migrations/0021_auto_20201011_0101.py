# Generated by Django 3.1.2 on 2020-10-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201010_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubeclip',
            name='contain_bad_content',
        ),
        migrations.RemoveField(
            model_name='youtubeclip',
            name='status',
        ),
        migrations.AddField(
            model_name='youtubeclip',
            name='bad_content_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Đang bóc băng'), (2, 'Kiểm tra đề cập lãnh đạo'), (3, 'Phân tích nội dung'), (4, 'Bình thường'), (5, 'Cần kiểm tra'), (6, 'Xấu độc')], default=5, verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='youtubeclip',
            name='live_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Đang kiểm tra'), (1, 'Die-YT'), (2, 'Gov-YT'), (3, 'Live-YT'), (4, 'Bad Link')], default=5, verbose_name='Trạng thái'),
        ),
    ]
