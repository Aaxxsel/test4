from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import PostSite


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    posts = PostSite.objects.all()
    context = {
        'Title': 'Главная страница',
        'posts': posts,
        'form': form
    }
    return render(request, 'blog/index.html', context)
