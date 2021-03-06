# Generated by Django

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers

class Migration(migrations.Migration):
    initial = True
#    dependencies = [
#        ('dcim', '0122_standardize_name_length'),
#        ('extras', '0053_rename_webhook_obj_type'),
#        ('circuits', '0024_standardize_name_length'),
#        ('tenancy', '0011_standardize_name_length'),
#    ]
    operations = [
        migrations.CreateModel(
            name='PBX',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, null=True, max_length=200)),
                ('pbx_type', models.CharField(max_length=50)),
                ('is_virtual', models.BooleanField()),
                ('domain', models.CharField(blank=True, null=True, max_length=200)),
                ('protocol', models.CharField(blank=True, null=True,max_length=50)),
                ('port', models.PositiveIntegerField(blank=True, null=True)),
                ('sip_proxy1', models.CharField(blank=True, null=True, max_length=200)),
                ('sip_proxy2', models.CharField(blank=True, null=True, max_length=200)),
                ('assigned_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('assigned_object_type', models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'interface')), models.Q(('app_label', 'virtualization'), ('model', 'vminterface')), _connector='OR')), null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pbx_assign', to='contenttypes.contenttype')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pbx_region_set', to='dcim.region')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pbx_site_set', to='dcim.site')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]