# Generated by Django 5.0.3 on 2024-05-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachmentor_app', '0015_remove_choice_text_en_remove_choice_text_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(default=''),
        ),
    ]
