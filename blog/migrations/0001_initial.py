# Generated by Django 4.2.3 on 2023-09-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='image')),
                ('views_count', models.IntegerField(default=0, verbose_name='views')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date_published')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ['date_published'],
            },
        ),
    ]
