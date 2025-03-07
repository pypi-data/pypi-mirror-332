# Generated by Django 4.2.15 on 2024-10-22 12:40

from django.db import connection, migrations, models, transaction
import django.db.models.deletion


def migrate_data_from_old_model_to_new_model_up(apps, schema_editor):
    """ Move objects from FileDistribution to NewFileDistribution."""
    FileDistribution = apps.get_model('file', 'FileDistribution')
    NewFileDistribution = apps.get_model('file', 'NewFileDistribution')
    for file_distribution in FileDistribution.objects.all():
        with transaction.atomic():
            NewFileDistribution(
                pulp_id=file_distribution.pulp_id,
                pulp_created=file_distribution.pulp_created,
                pulp_last_updated=file_distribution.pulp_last_updated,
                pulp_type=file_distribution.pulp_type,
                name=file_distribution.name,
                base_path=file_distribution.base_path,
                content_guard=file_distribution.content_guard,
                remote=file_distribution.remote,
                publication=file_distribution.publication
            ).save()
            file_distribution.delete()


def migrate_data_from_old_model_to_new_model_down(apps, schema_editor):
    """ Move objects from NewFileDistribution to FileDistribution."""
    FileDistribution = apps.get_model('file', 'FileDistribution')
    NewFileDistribution = apps.get_model('file', 'NewFileDistribution')
    for file_distribution in NewFileDistribution.objects.all():
        with transaction.atomic():
            FileDistribution(
                pulp_id=file_distribution.pulp_id,
                pulp_created=file_distribution.pulp_created,
                pulp_last_updated=file_distribution.pulp_last_updated,
                pulp_type=file_distribution.pulp_type,
                name=file_distribution.name,
                base_path=file_distribution.base_path,
                content_guard=file_distribution.content_guard,
                remote=file_distribution.remote,
                publication=file_distribution.publication
            ).save()
            file_distribution.delete()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('file', '0008_add_manifest_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFileDistribution',
            fields=[
                ('distribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_filedistribution', serialize=False, to='core.distribution')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.distribution',),
        ),
        migrations.RunPython(
            code=migrate_data_from_old_model_to_new_model_up,
            reverse_code=migrate_data_from_old_model_to_new_model_down,
            elidable=True,
        ),
        migrations.DeleteModel(
            name='FileDistribution',
        ),
        migrations.RenameModel(
            old_name='NewFileDistribution',
            new_name='FileDistribution',
        ),
    ]
