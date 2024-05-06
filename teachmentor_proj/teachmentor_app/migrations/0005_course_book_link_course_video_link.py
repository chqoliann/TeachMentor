# Generated by Django 5.0.3 on 2024-04-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachmentor_app', '0004_course_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='book_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='video_link',
            field=models.URLField(blank=True),
        ),
    ]