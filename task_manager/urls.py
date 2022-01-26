from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render


existing_tasks = ["default values"]
completed_tasks = []


def index(request):
    return render(request, "index.html", {"tasks": existing_tasks})


def completed_task_view(request):
    return render(request, "completed.html", {"tasks": completed_tasks})


def all_tasks_view(request):
    return render(
        request,
        "all.html",
        {"tasks": {"completed": completed_tasks, "existing": existing_tasks}},
    )


def add_task_view(request):
    existing_tasks.append(request.GET.get("task"))
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, index):
    origin = request.headers.get("Referer").split("/")[-2]
    del existing_tasks[index - 1]
    return HttpResponseRedirect(f"/{origin}/")


def complete_task_view(request, index):
    origin = request.headers.get("Referer").split("/")[-2]
    completed = existing_tasks.pop(index - 1)
    completed_tasks.append(completed)
    return HttpResponseRedirect(f"/{origin}/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", index),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>", delete_task_view),
    path("complete_task/<int:index>", complete_task_view),
    path("completed_tasks/", completed_task_view),
    path("all_tasks/", all_tasks_view),
]
