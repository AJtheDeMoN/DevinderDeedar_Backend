# Generated by Django 4.1.13 on 2024-05-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='title_punjabi',
        ),
        migrations.RemoveField(
            model_name='article',
            name='published_date',
        ),
        migrations.AddField(
            model_name='article',
            name='title_english',
            field=models.CharField(default='english', max_length=200),
        ),
    ]