from django.shortcuts import render
from .models import Member  # Import your Member model

def index(request):  # This is line 5
    obj = Member.objects.all()  # This line needs to be indented
    return render(request, 'index.html', {'data': obj})