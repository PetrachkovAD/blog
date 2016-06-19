from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


def articale_list(request):
    articales = Blog.objects.filter(isReady=True)
    return render(request, 'main/articale_list.html', {'articales': articales})


def articale_detail(request, pk):
    articale = get_object_or_404(Blog, pk=pk)
    return render(request, 'main/articale_detail.html', {'articale': articale})


def articale_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            articale = form.save()
            return redirect('main.views.articale_detail', pk=articale.pk)
    else:
        form = BlogForm()
    return render(request, 'main/articale_edit.html', {'form': form})


def articale_edit(request, pk):
    articale = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=articale)
        if form.is_valid():
            articale = form.save()
            return redirect('main.views.articale_detail', pk=articale.pk)
    else:
        form = BlogForm(instance=articale)
    return render(request, 'main/articale_edit.html', {'form': form})


def articale_search(request):
    if 'searchString' in request.GET:
        articales = Blog.objects.filter(headerArticale__icontains=request.GET['searchString'], isReady=True)\
            .filter(articale__icontains=request.GET['searchString'],
                    isReady=True)
        return render(request, 'main/articale_list.html',
                      {'articales': articales,
                       'searchString': request.GET['searchString']})
    else:
        articales = Blog.objects.filter(isReady=True)
    return render(request, 'main/articale_list.html', {'articales': articales})
