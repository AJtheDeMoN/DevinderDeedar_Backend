# Generated by Django 4.1.13 on 2024-05-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_book_english_article_book_punjabi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='book_punjabi',
            field=models.CharField(default='ਅਖਬਾਰ ਦੇ ਲੇਖ', max_length=100),
        ),
    ]
