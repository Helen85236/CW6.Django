# Generated by Django 4.2.3 on 2023-09-06 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_blocked', 'Can blocked'), ('viewed_list', 'Can viewed_list')]},
        ),
    ]
