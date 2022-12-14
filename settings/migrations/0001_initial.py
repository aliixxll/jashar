# Generated by Django 4.1.1 on 2022-09-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=100)),
                ('descriptin_site', models.CharField(max_length=255)),
                ('logo_site', models.ImageField(upload_to='logo/')),
                ('phone_site', models.CharField(max_length=100)),
                ('email_site', models.EmailField(max_length=254)),
                ('adress_site', models.CharField(max_length=100)),
                ('wark_time_site', models.CharField(max_length=200)),
                ('facebook_site', models.URLField()),
                ('twitter_site', models.URLField()),
                ('instagram_site', models.URLField()),
                ('linkedin_site', models.URLField()),
            ],
        ),
    ]
