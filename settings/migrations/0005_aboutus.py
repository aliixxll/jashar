# Generated by Django 4.1.1 on 2022-10-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_setting_image_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about_us/')),
                ('video_url', models.URLField()),
            ],
        ),
    ]