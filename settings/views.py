from django.shortcuts import render, redirect
from django.core.mail import send_mail
from settings.models import Setting, AboutUs, Team, News, Contact

# Create your views here.
def index(reguest):
    setting = Setting.objects.latest('id')
    about_us = AboutUs.objects.latest("id")
    context = {
        'setting' : setting,
        'about_us': about_us
    }
    return render(reguest, 'index.html', context)

def team_index(request):
    setting = Setting.objects.latest('id')
    teams = Team.objects.all()
    context = {
        'teams': teams,
        'setting': setting,
    }     
    return render(request, 'team.html', context)

def team_detail(request,id):
    setting = Setting.objects.latest('id')
    team = Team.objects.get(id = id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail( 
            #subject 
            "С вами пытались связаться", 
            #message 
            f"Здравствуйте {team.name_and_surname}, с вами хотят связаться. Человек {name}, с почтой {email}, с номером {phone}, тема {subject}, сообщение {message}", 
            #from email 
            'noreply@somehost.local', 
            #to email 
            [team.email] 
        ) 
        send_mail( 
            #subject 
            f"{name} ваше сообщение удачно отправлено", 
            #message  
            f"{name} ваше сообщение которое вы писали для {team.name_and_surname} успешно отправлено. Ожидайте ответа", 
            #from email 
            'noreply@somehost.local', 
            #to email 
            [email] 
        ) 
        return redirect('index')

    context = {
        'team': team,
        'setting': setting,
    }
    return render(request, 'team-details.html', context)

def news_index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    context = {
        'news': news,
        'setting': setting,
    }
    return render(request, 'news.html', context)
    
def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news = News.objects.get(id = id)
    context = {
        'setting': setting,
        'news': news,
    }
    return render(request, 'news-details.html', context)

def contact(request): 
    setting = Setting.objects.latest('id')  
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name = name, email = email, number= phone, subject = subject, message = message)
        send_mail(
            f'{subject}',
            f'{name} Здравствуйте,спасибо за отклик.Мы с вами скоро свяжемся.Ваше сообщение:{message}. Ваши контакты:{phone}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    context = {
        'setting': setting,
    }
    return render(request, 'contact.html', context)