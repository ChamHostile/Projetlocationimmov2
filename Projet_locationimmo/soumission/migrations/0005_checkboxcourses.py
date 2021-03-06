# Generated by Django 3.1.4 on 2021-01-06 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soumission', '0004_signercli'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkboxcourses',
            fields=[
                ('cb_id', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=100)),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soumission.clientcli', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'check box courses',
                'db_table': 'CheckBox_Cli',
                'managed': True,
            },
        ),
    ]
