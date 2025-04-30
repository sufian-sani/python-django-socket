from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

@login_required
def home(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/home.html', {'users': users})

@login_required
def chat_room(request, username):
    other_user = User.objects.get(username=username)
    return render(request, 'chat/chat_room.html', {'other_user': other_user})
