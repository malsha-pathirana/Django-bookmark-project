from django.shortcuts import render, redirect
from .models import Bookmark


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        category = request.POST.get('category')

        Bookmark.objects.create(title=title, url=url, category=category)
        return redirect('index')

    bookmarks = Bookmark.objects.all()
    return render(request, 'index.html', {"bookmarks": bookmarks})


def delete_bookmark(request, id):
    bookmark = Bookmark.objects.get(id=id)
    bookmark.delete()
    return redirect('index')
