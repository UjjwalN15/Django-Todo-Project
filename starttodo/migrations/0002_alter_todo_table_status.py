# Generated by Django 5.0.6 on 2024-05-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starttodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_table',
            name='Status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Not started', 'Not started'), ('Completed', 'Completed')], max_length=200),
        ),
    ]
