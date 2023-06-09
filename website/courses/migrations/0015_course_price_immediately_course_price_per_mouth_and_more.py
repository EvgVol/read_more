# Generated by Django 4.2.1 on 2023-07-13 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_course_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price_immediately',
            field=models.PositiveIntegerField(default=0, verbose_name='price immediately'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='price_per_mouth',
            field=models.PositiveIntegerField(default=0, verbose_name='price per mouth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advantage',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('additional_text', models.TextField(verbose_name='additional text')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_courses', to='courses.course', verbose_name='course')),
            ],
            options={
                'verbose_name': 'card',
                'verbose_name_plural': 'cards',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='cards',
            field=models.ManyToManyField(related_name='course_cards', to='courses.card', verbose_name='cards'),
        ),
    ]
