from django.shortcuts import render, redirect
from .models import boards
# Create your views here.
def index(request):
    board = boards.objects.all()
    return render(request, 'boards/index.html', {'board':board})
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    board = boards()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('/boards/')
    
def detail(request, pk):
    board = boards.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board':board})
    
def edit(request, pk):
    board = boards.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board':board})
    
def update(request, pk):
    board = boards.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('/boards/')
    
def delete(request, pk):
    board = boards.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')