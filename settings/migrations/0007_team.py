# Generated by Django 4.1.1 on 2022-10-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_alter_aboutus_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='team_image/')),
                ('name_and_surname', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
