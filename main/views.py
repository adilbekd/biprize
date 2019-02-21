from django.shortcuts import render
from django.http import HttpResponse 

from django.contrib import auth
from django.shortcuts import redirect

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import User
import random
from threading import Timer

def index(request):
    return render(request, 'main/home.html')

'''
def sendEmail(to):
    subject = 'Subject'
    html_message = render_to_string('main/mail_template.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    from_email = 'From <adilbekdos@gmail.com>'

    mail.send_mail(subject, plain_message, from_email, [to],html_message=html_message)
'''
start = 0
sec = 60

def timeout():
    sec = 0

def winners(request):
    all_Users = User.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        if name == "flagman123":
            start = 1
        email = request.POST['email']
        city = request.POST['city']
        timee = request.POST['time']
        p = User(name=name, email=email, city=city)
        print('@'*90)
        print(all_Users)
        print('@'*90)
        print(timee)
        print('@'*90)
        p.save()
        for p in User.objects.all():
            print(p)

    if start:
        t = Timer(1 * 60, timeout)
        t.start()

    if sec==0:
        html = ''
        numWinners = 2
        numUsers = all_Users.count()-1
        listWinners = set()
        listWinners2 = []

        while len(listWinners)<numWinners:
            listWinners.add(all_Users[random.randint(0,numUsers)].email)

        for i in listWinners:
            for j in all_Users:
                if j.email == i:
                    #sendEmail(i)
                    listWinners2.append(j)
                    break


        context={'winnersTable': listWinners2}

        return render(request, 'main/wrapper.html', context)
    if sec>0:
        return render(request, 'main/wrapper2.html')
'''
class UserCreate(CreateView):
    form = PostForm(request.POST)
    post = form.save()
'''