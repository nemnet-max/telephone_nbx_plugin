# Generated by Django

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers

class Migration(migrations.Migration):

    dependencies = [
        ('phonebox_plugin', '0001_pbx'),
        ('dcim', '0122_standardize_name_length'),
        ('extras', '0053_rename_webhook_obj_type'),
        ('circuits', '0024_standardize_name_length'),
        ('tenancy', '0011_standardize_name_length'),
    ]
    operations = [
        migrations.CreateModel(
            name='VoiceCircuit',
            fields=[
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('pbx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_pbx_set', to='phonebox_plugin.pbx')),
                ('voice_circuit_type', models.CharField(max_length=50)),
                ('provider_circuit_id', models.CharField(blank=True, max_length=50)),
                ('sip_source', models.CharField(blank=True, max_length=200)),
                ('sip_target', models.CharField(blank=True, max_length=200)),
                ('assigned_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('assigned_object_type', models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'interface')), models.Q(('app_label', 'virtualization'), ('model', 'vminterface')), _connector='OR')), null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.contenttype')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_provider_set', to='circuits.provider')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_region_set', to='dcim.region')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_site_set', to='dcim.site')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]