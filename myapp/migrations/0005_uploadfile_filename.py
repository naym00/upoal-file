# Generated by Django 5.0.1 on 2024-01-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]