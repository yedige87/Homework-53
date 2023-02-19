from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ToDo

actions = [{'id': '0', 'action': 'выберите действие'}, {'id': '1', 'action': 'добавить задачу'},
           {'id': '2', 'action': 'удалить задачу'}, {
               'id': '3', 'action': 'редактировать задачу'},
           {'id': '4', 'action': 'показать задачу'}]
states = [{'id': '0', 'state': 'new', 'rus': 'Новая задача'}, {'id': '1', 'state': 'processing', 'rus': 'В процессе выполнения'},
          {'id': '2', 'state': 'complited', 'rus': 'Задача завершена'}]


def index_view(request: WSGIRequest):
    if request.method == "GET":
        todos = ToDo.objects.all().order_by('id')
        context = {'todos': todos, 'actions': actions, 'states': states}
        return render(request, 'index.html', context=context)
    print(request.POST)
    action = request.POST.get('action')
    task = request.POST.get('task')
    action = int(action)
    print("action - ", action)

    if not task:
        task = '0'
    task = int(task)
    print("task - ", task)

    if action == 1:
        context = {'states': states}
        return render(request, 'add.html', context=context)
    if action != 0 and task != 0:
        todo = get_object_or_404(ToDo, pk=task)
        if action == 2 and task != 0:
            todo.delete()
        elif action == 3 and task != 0:
            return redirect('todo_edit', pk=todo.id)
        elif action == 4 and task != 0:
            return redirect('todo_view', pk=todo.id)

    todos = ToDo.objects.all().order_by('id')
    return render(request, 'index.html', context={'todos': todos, 'actions': actions})
