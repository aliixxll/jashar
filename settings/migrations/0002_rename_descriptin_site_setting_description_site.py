# Generated by Django 4.1.1 on 2022-09-29 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='descriptin_site',
            new_name='description_site',
        ),
    ]
