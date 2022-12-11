import datetime
from user.models import *
from user.forms import RegistrationForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.save()
            print(form.cleaned_data['user_role'])
            # user_role = request.POST.get('user_role')
            try:
                group = Group.objects.create(name=form.cleaned_data['user_role'])
            except:
                group = Group.objects.get(name=form.cleaned_data['user_role'])
            user.groups.add(group)
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('user:login_user')

    context = {'form':form}
    return render(request, 'user_register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("news:news")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            # messages.info(request, 'Username atau Password salah!')
            return JsonResponse({
                "status": False,
                "message": "Login gagal, Username atau Password salah!"
            }, status=401)
    context = {}
    return render(request, 'user_login.html', context)

# User logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("news:news"))
    response.delete_cookie('last_login')
    return response

# Menunjukkan profile user
def user_profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)

# Menambahkan notes pada profile user
@login_required
def add_notes(request):
    if request.method == 'POST':
        notes = Notes(
           user=request.user,
            comment=request.POST.get('comment')
        )
        notes.save()
        return JsonResponse({
            'user': notes.user.username,
            'comment': notes.comment
        })
    return render(request, 'profile.html', {})

@login_required
def show_comment(request):
    data = Notes.objects.all()
    print(data)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
