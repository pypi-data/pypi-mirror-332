# Generated by Django 2.2.3 on 2019-07-24 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_increase_artifact_size_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='completed',
        ),
    ]
