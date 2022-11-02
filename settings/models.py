from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.
class Setting(models.Model):
    name_site = models.CharField(max_length=100)
    description_site = models.CharField(max_length=255)
    logo_site = models.ImageField(upload_to = 'logo/')
    phone_site = models.CharField(max_length = 100)
    email_site = models.EmailField()
    address_site = models.CharField(max_length = 100)
    wark_time_site = models.CharField(max_length=200)
    image_site = models.ImageField(upload_to = 'setting_image/')
    facebook_site = models.URLField()
    twitter_site = models.URLField()
    instagram_site = models.URLField()
    linkedin_site = models.URLField()


    def __str__(self):
        return self.name_site

class AboutUs(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'about_us/')
    video_url = models.FileField(upload_to ='video/')

    def __sts__(self):
        return self.title



class Team(models.Model):
    photo = models.ImageField(upload_to = 'team_image/') 
    name_and_surname = models.CharField(max_length = 100)  
    job = models.CharField(max_length = 50)    
    description = models.CharField(max_length = 200)
    phone =models.CharField(max_length = 30)
    email = models.EmailField()
    location = models.CharField(max_length = 100)
    age = models.PositiveSmallIntegerField()
    language = models.CharField(max_length = 255)
    experience = models.CharField(max_length = 255)
    availability = models.CharField(max_length = 255)

    def __str__(self):
        return self.name_and_surname

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"  

class News(models.Model):
    title_news = models.CharField(max_length = 100)
    description = models.TextField()
    image_news = models.ImageField(upload_to = 'image_news/')
    created_news = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title_news

    class Meta:
        verbose_name = "Новость"  
        verbose_name_plural = "Новости" 

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    number = models.CharField(max_length =50)
    email = models.EmailField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}{self.subject}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"    

        
          




