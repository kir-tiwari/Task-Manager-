from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todo.models import TODO
from django.shortcuts import get_object_or_404


def welcome(request):
    return render(request, 'welcome.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = email.lower().strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email.lower().strip(),
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('todo')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')



@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODO.objects.create(title=title, user=request.user)

    todos = TODO.objects.filter(user=request.user).order_by('-date')

    total = todos.count()
    completed = todos.filter(completed=True).count()
    pending = todos.filter(completed=False).count()

    return render(request, 'todo.html', {
        'todos': todos,
        'total': total,
        'completed': completed,
        'pending': pending,
    })

@login_required(login_url='login')
def delete_todo(request, pk):
    todo = get_object_or_404(TODO, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo')
@login_required(login_url='login')
def toggle_todo(request, pk):
    todo = get_object_or_404(TODO, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')
@login_required(login_url='login')
def toggle_complete(request, pk):
    todo = get_object_or_404(TODO, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')

