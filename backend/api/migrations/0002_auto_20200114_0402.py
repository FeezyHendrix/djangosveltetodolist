# Generated by Django 3.0.2 on 2020-01-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
