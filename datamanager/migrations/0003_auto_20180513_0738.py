# Generated by Django 2.0.4 on 2018-05-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanager', '0002_auto_20180513_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitydividend',
            name='dividend_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]