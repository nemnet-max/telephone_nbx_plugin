# Generated by Django

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers

class Migration(migrations.Migration):

    dependencies = [
        ('telephone_plugin', '0002_voice_circuits'),
        ('dcim', '0122_standardize_name_length'),
        ('extras', '0053_rename_webhook_obj_type'),
        ('circuits', '0024_standardize_name_length'),
        ('tenancy', '0011_standardize_name_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('number', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^\\+?[0-9A-D\\#\\*]*$', 'Numbers can only contain: leading +, digits 0-9; chars A, B, C, D; # and *')])),
                ('fio', models.CharField(blank=True, null=True, max_length=200)),
                ('pbx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_pbx_set', to='telephone_plugin.pbx')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_device_set', to='dcim.device')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_region_set', to='dcim.region')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_site_set', to='dcim.site')),
                ('tenantgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenantgroup')),
                ('tenant', models.ForeignKey(blank=True, null=True,on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('forward_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_forward_to_set', to='telephone_plugin.number')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_provider_set', to='circuits.provider')),
                ('is_record', models.BooleanField()),
                ('access_cat', models.CharField(blank=True, null=True, max_length=32)),
                ('comment', models.CharField(blank=True, null=True, max_length=200)),
                ('assigned_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('assigned_object_type', models.ForeignKey(blank=True,
                                                           limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'interface')),)),
                                                           null=True, on_delete=django.db.models.deletion.PROTECT,
                                                           related_name='number_assign',
                                                           to='contenttypes.contenttype')),
                ('description', models.CharField(blank=True, null=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='number',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]