# Generated by Django 4.2 on 2023-04-13 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0017_alter_daiira_wilaya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daiira',
            name='wilaya',
        ),
    ]
