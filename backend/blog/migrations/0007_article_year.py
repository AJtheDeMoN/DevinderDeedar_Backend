# Generated by Django 4.1.13 on 2024-05-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_book_punjabi'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]