# Generated by Django 4.2.1 on 2023-07-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(upload_to='courses/technologies/images/', verbose_name='image'),
        ),
    ]
