# Generated by Django 3.2.12 on 2022-04-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1991-12-01'),
            preserve_default=False,
        ),
    ]
