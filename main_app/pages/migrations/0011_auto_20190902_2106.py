# Generated by Django 2.2.4 on 2019-09-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20190902_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract_details',
            name='phone_number',
            field=models.CharField(default='01794895700', max_length=23),
        ),
    ]