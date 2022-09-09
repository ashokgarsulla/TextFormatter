from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import CreatePost
from .models import Post
def create_post(request):
    if request.method == 'POST':
        fm = CreatePost(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data["title"])
            print(fm.cleaned_data["body"])
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = CreatePost(auto_id=True)
    return render(request,"app/create_post.html",{"form":fm})

def list_post(request):
    post_data = Post.objects.all()
    for i in post_data:
        print(i.title)
    return render(request,"app/post_list.html",{"post":post_data})