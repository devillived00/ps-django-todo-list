# Generated by Django 3.2.12 on 2022-05-04 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('hired_from', models.DateField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(max_length=500)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('position', models.CharField(choices=[('jp', 'Junior Python Developer'), ('rp', 'Regular Python Developer'), ('sp', 'Senior Python Developer'), ('po', 'Project Owner'), ('an', 'Analyst'), ('te', 'Tester')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('state', models.BooleanField(default=False)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Internal Task', 'IT'), ('Helpdesk Task', 'HT'), ('Project Task', 'PT')], max_length=20)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
            options={
                'ordering': ['state'],
            },
        ),
    ]
