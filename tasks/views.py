from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'La contraseñas no coinciden'
        })


def tasks(request):
    tasks=Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks
    })


def singout(request):
    logout(request)
    return redirect('home')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user=authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
            'form': AuthenticationForm,
            'error':'El usuario no ha sido creado'
            })
        else:
            login(request, user)
            return redirect('tasks')

def deletetasks(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


def CreateTask(request):
    if request.method == 'POST':
        try:
            form=TaskForm(request.POST)
            nueva_tarea=form.save(commit=False)
            nueva_tarea.user=request.user
            nueva_tarea.save()
            return redirect('tasks')
        except:
             return render(request,'create_task.html',{
            'form': TaskForm,
            'error':"hubo un error"
        })

    else:  
        return render(request,'create_task.html',{
            'form': TaskForm
        })

def TaskDetails(request,id):
    if request.method == 'GET':
        task=get_object_or_404(Task,id=id)
        form= TaskForm(instance=task)
        print(id)
        return render(request,'task_detail.html',{'tarea':task,'form':form})
    else:
        task=get_object_or_404(Task,id=id)
        form=TaskForm(request.POST,instance=task)
        form.save()
        return redirect('tasks')

        


