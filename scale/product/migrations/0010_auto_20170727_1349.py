# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-27 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20170301_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileancestrylink',
            name='job_exe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_exe_file_links', to='job.JobExecution'),
        ),
    ]
