# Generated by Django 2.2.4 on 2019-09-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20190902_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='agent_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_agents', models.CharField(default='', max_length=50)),
                ('our_angets_details', models.CharField(default='', max_length=200)),
                ('our_agent_name', models.CharField(default='', max_length=50)),
                ('our_agnet_type', models.CharField(default='', max_length=50)),
                ('our_agent_details', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='contract_details',
            name='our_agents',
        ),
        migrations.RemoveField(
            model_name='contract_details',
            name='our_angets_details',
        ),
    ]