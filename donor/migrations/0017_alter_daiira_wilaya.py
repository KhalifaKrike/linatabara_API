# Generated by Django 4.2 on 2023-04-13 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0016_daiira_wilaya_alter_donor_blood_alter_donor_daiira_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daiira',
            name='wilaya',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='donor.wilaya'),
        ),
    ]
