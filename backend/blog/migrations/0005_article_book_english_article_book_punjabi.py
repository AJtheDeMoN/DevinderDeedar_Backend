# Generated by Django 4.1.13 on 2024-05-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_title_article_title_punjabi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='book_english',
            field=models.CharField(default='book', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='book_punjabi',
            field=models.CharField(default='book', max_length=100),
        ),
    ]