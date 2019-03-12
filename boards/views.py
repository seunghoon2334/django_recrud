from django.shortcuts import render, redirect
from .models import boards, Comment
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
    
def detail(request, board_pk):
    board = boards.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {
        'board':board,
        'comments':comments
    }
    return render(request, 'boards/detail.html', context)
    
def edit(request, board_pk):
    if request.method == 'POST':
        board = boards.objects.get(pk=board_pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        board = boards.objects.get(pk=board_pk)
        return render(request, 'boards/edit.html', {'board':board})
    
# def update(request, board_pk):
#     board = boards.objects.get(pk=board_pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)
    
def delete(request, board_pk):
    board = boards.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
        
def comment_create(request, board_pk):
    # 1. 댓글 달 게시물을 가져온다.
    board = boards.objects.get(pk=board_pk)
    # 2. 댓글을 저장한다.
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.board = board
    comment.save()
    return redirect('boards:detail', board.pk)