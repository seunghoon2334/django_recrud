from django.shortcuts import render, redirect
from .models import boards
# Create your views here.
def index(request):
    board = boards.objects.all()
    return render(request, 'boards/index.html', {'board':board})
    
def new(request):
    if request.method == 'POST':
        board = boards()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')
    
# def create(request):
#     board = boards()
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)
    
def detail(request, pk):
    board = boards.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board':board})
    
def edit(request, pk):
    if request.method == 'POST':
        board = boards.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        board = boards.objects.get(pk=pk)
        return render(request, 'boards/edit.html', {'board':board})
    
# def update(request, pk):
#     board = boards.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)
    
def delete(request, pk):
    board = boards.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)