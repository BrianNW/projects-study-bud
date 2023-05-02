from django.shortcuts import render
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Other room'},
]

def home(request):
    return render(request, 'home.html')

def room(request):    
    return render(request, 'room.html')