# Generated by Django 4.1.7 on 2023-02-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_datecomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creadodate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
