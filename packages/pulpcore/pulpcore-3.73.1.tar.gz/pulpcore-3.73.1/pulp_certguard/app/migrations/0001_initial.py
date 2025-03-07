# Generated by Django 4.2.15 on 2024-10-22 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0091_systemid'),
    ]

    operations = [
        migrations.CreateModel(
            name='RHSMCertGuard',
            fields=[
                ('contentguard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='certguard_rhsmcertguard', serialize=False, to='core.contentguard')),
                ('ca_certificate', models.TextField()),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.contentguard',),
        ),
        migrations.CreateModel(
            name='X509CertGuard',
            fields=[
                ('contentguard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='certguard_x509certguard', serialize=False, to='core.contentguard')),
                ('ca_certificate', models.TextField()),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.contentguard',),
        ),
    ]
