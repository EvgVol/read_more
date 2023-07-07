# Generated by Django 4.2.1 on 2023-06-29 07:10

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video_text_image_file_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order'], 'verbose_name': 'content', 'verbose_name_plural': 'contents'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order'], 'verbose_name': 'module', 'verbose_name_plural': 'modules'},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]