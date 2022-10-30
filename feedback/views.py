from django.shortcuts import render, redirect
from R_designer.forms import FeedBackForm
from django.views.generic import View
from django.contrib import messages
from R_designer import settings
from tele.telegramm import send_message
from datetime import *

def home(request):
    return render(request, 'home.html')

msk = timedelta(hours = 3)
dt = datetime.now() + msk

class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MY_INFO, 'Заявка создана успешно.')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = "*ЗАЯВКА С САЙТА:*" + "\n" + "Дата заявки: " + str(dt.strftime("%d.%m.%Y")) + "\n" + "Время заявки: " + str(dt.strftime("%H:%M")) + "\n" + "Имя: " + str(name) + "\n" + "Телефон: " + str(phone)
            send_message(message)
        else:
            messages.add_message(request, settings.MY_INFO, 'Что-то пошло не так.')
        return redirect("/")



