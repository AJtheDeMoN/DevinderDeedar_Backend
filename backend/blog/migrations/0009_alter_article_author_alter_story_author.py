# Generated by Django 4.1.13 on 2024-05-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_prose_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default='ਦੇਵਿੰਦਰ ਦੀਦਾਰ', max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.CharField(default='ਦੇਵਿੰਦਰ ਦੀਦਾਰ', max_length=100),
        ),
    ]
