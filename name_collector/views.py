from django.shortcuts import render

from name_collector.models import User


def index(request):
    message = ''
    if request.method == "POST":
        u = User(name=request.POST.get("name"))
        if u.name in tuple(i.name for i in User.objects.all()):
            message = f'Уже виделись, {u.name}'
        else:
            message = f'Привет, {u.name}'
            u.save()
    return render(request, "name_collector/index.html", {"message": message})


def userlist(request):
    users = User.objects.all()
    return render(request, "name_collector/userlist.html", {"users": users})
