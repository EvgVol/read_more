# Generated by Django 4.2.1 on 2023-05-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_blog_post_publish_bb7600_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique_for_date='publish', verbose_name='Slug'),
        ),
    ]