# Generated by Django 2.1.15 on 2019-12-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]