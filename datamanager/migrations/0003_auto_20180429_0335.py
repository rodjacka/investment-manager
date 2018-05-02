# Generated by Django 2.0.4 on 2018-04-29 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datamanager', '0002_auto_20180429_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityCLass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_class', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='notetypes',
            options={'verbose_name_plural': 'notetypes'},
        ),
        migrations.AlterModelOptions(
            name='portfoliosecurity',
            options={'verbose_name_plural': 'portfoliosecurities'},
        ),
        migrations.AlterModelOptions(
            name='security',
            options={'verbose_name_plural': 'securities'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'settings'},
        ),
        migrations.AlterField(
            model_name='settings',
            name='setting_numerical_value',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='setting_text_value',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='security',
            name='security_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datamanager.SecurityCLass'),
            preserve_default=False,
        ),
    ]