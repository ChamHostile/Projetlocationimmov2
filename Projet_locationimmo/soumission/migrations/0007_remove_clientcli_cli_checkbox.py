# Generated by Django 3.1.4 on 2021-01-06 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soumission', '0006_auto_20210106_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcli',
            name='cli_checkbox',
        ),
    ]