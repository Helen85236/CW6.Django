# Generated by Django 4.2.3 on 2023-09-02 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trial',
            options={'ordering': ['date'], 'verbose_name': 'trial', 'verbose_name_plural': 'trials'},
        ),
        migrations.AddField(
            model_name='trial',
            name='client',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='newsletters.client', verbose_name='client'),
            preserve_default=False,
        ),
    ]
