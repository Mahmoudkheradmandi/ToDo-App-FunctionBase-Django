from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
        return redirect("todo:home")

    context = {"tasks": tasks, "form": form}
    return render(request, "todo.html", context)


@login_required
def update(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect("todo:home")

    context = {"form": form}

    return render(request, "update.html", context)


@login_required
def complete(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.complete = True
    item.save()
    return redirect("todo:home")


@login_required
def delete(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.delete()
    return redirect("todo:home")