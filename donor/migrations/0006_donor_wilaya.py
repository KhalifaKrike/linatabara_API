# Generated by Django 4.2 on 2023-04-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_donor_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='wilaya',
            field=models.CharField(blank=True, choices=[(2, 'chlef')], max_length=30),
        ),
    ]
