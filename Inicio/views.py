from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def inicioadmin(request):
    return render(request,'Inicio/admin.html')

@login_required
def inicionormal(request):
    return render(request,'Inicio/normal.html')

