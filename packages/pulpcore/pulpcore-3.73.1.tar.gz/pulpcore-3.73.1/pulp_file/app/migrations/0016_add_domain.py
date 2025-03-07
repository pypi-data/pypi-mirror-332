# Generated by Django 3.2.15 on 2022-09-15 02:20

from django.db import migrations, models
import django.db.models.deletion
import pulpcore.app.util


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0102_add_domain_relations'),
        ('file', '0015_allow_null_manifest'),
    ]

    operations = [
        migrations.AddField(
            model_name='filecontent',
            name='_pulp_domain',
            field=models.ForeignKey(default=pulpcore.app.util.get_domain_pk, on_delete=django.db.models.deletion.PROTECT, related_name='file_filecontent', to='core.domain'),
        ),
        migrations.AlterUniqueTogether(
            name='filecontent',
            unique_together={('relative_path', 'digest', '_pulp_domain')},
        ),
    ]
