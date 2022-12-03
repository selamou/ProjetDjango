from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home (request) :
    boards= Board.objects.all()
    boards_name = []
    for board in boards :
        boards_name.append(board.name)
    print(boards_name)
    return render(request,'home.html',{'board':boards})
# Create your views here.
