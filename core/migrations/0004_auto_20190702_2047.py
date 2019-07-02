# Generated by Django 2.2.2 on 2019-07-02 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190702_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyrecord',
            name='text',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='achieved',
            field=models.IntegerField(help_text='How many X did you today?', null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='habit',
            name='target',
            field=models.IntegerField(help_text='How many is your target?', null=True),
        ),
    ]
