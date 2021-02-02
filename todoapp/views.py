from django.shortcuts import render
from django.contrib.auth.models import User

def index(request, user_id):
    user = User.objects.get(pk=user_id)
    todos = user.todo.objects.all()[:10] 
    context = {
        'todos':todos
    }
    return render(request, 'todoapp/index.html', context)


def details(request, id, user_id):
    user = User.objects.get(pk=user_id)
    todo = user.todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todoapp/details.html', context)


def add(request, user_id):
    user = User.objects.get(pk=user_id)
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = user.todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')