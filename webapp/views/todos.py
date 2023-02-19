from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import ToDo

states = [{'id': '0', 'state': 'new', 'rus': 'Новая задача'}, {'id': '1', 'state': 'processing', 'rus': 'В процессе выполнения'},
          {'id': '2', 'state': 'complited', 'rus': 'Задача завершена'}]


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'add.html', context={'states': states})
    print(request.POST)
    todo_data = {
        'id': request.POST.get('id'),
        'title': request.POST.get('title'),
        'date_todo': request.POST.get('date_todo'),
        'state': request.POST.get('state'),
        'description': request.POST.get('description'),
    }
    # 'state_id': int(request.POST.get('state_id')),
    todo = ToDo.objects.create(**todo_data)
    return redirect(reverse('todo_view', kwargs={'pk': todo.pk}))


def todo_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'view.html', context={'todo': todo})
