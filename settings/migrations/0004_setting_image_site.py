# Generated by Django 4.1.1 on 2022-10-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_rename_adress_site_setting_address_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='image_site',
            field=models.ImageField(default=0, upload_to='setting_image/'),
            preserve_default=False,
        ),
    ]
