# Generated by Django 4.2.3 on 2023-09-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='comment'),
        ),
    ]