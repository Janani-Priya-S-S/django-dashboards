# Generated by Django 4.0.7 on 2022-10-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datorum_pipelines', '0002_taskresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskresult',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='payload',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
