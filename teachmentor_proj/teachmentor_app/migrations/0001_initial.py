# Generated by Django 5.0.3 on 2024-03-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
    ]
