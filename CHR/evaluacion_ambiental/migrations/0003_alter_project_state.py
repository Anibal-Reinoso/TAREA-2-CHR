# Generated by Django 4.1.7 on 2023-02-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion_ambiental', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado'),
        ),
    ]
