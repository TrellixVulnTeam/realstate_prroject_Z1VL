# Generated by Django 2.2.4 on 2019-09-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20190902_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract_details',
            name='Address_details',
            field=models.CharField(default='203 Fake St. Mountain View, San Francisco, California', max_length=100),
        ),
        migrations.AlterField(
            model_name='contract_details',
            name='phone_number',
            field=models.CharField(default='+1 232 3235 324', max_length=13),
        ),
    ]