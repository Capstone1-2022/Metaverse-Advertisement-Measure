from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Content
from .forms import ContentForm

def home(request):
    posts = Content.objects.all()
    return render(request, 'home.html', {'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return render(request, 'complete.html')
    else:
        form = ContentForm()
    return render(request, 'new.html',{'form':form})

def detail(request, index):
    post = get_object_or_404(Content, pk = index)
    return render(request, 'detail.html', {'post':post})

def delete(request,pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def complete(request, index):
    post = get_object_or_404(Content, pk = index)
    return render(request, 'complete.html', {'post':post})