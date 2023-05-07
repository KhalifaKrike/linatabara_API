# Generated by Django 4.2 on 2023-05-07 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0024_alter_donor_n_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='date_signup',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='donor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=1),
        ),
    ]