# Generated by Django 2.1.7 on 2019-04-23 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursematchapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='departement',
            new_name='department',
        ),
    ]
