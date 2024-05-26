# Generated by Django 4.1.13 on 2024-05-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prose',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title_punjabi', models.CharField(max_length=200)),
                ('title_english', models.CharField(default='english', max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=2024)),
            ],
        ),
    ]