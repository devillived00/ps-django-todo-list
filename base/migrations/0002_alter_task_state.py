# Generated by Django 3.2.12 on 2022-05-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.BooleanField(default=False, verbose_name='Done'),
        ),
    ]
