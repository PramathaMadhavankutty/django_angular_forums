from django.shortcuts import render
from .models import Magazine
from accounts.views import login_required


@login_required(login_url='/login/')
def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})