from django.shortcuts import render
from .forms import BlogpostForm
from .models import Blogpost, Comment
from django.http.response import HttpResponseRedirect
from blog.forms import CommentForm

def index(request):
    posts = Blogpost.objects.all().order_by("-id")
    return(render(request, "blog/index.html", {
    "posts" : posts,    
    }))
    
def post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            # blogpost = Blogpost(
            #     title = form.cleaned_data['title'],
            #     author = form.cleaned_data['author'],
            #     content = form.cleaned_data['content'])
            # blogpost.save()
            form.save()
            return HttpResponseRedirect("/")
        
    else:
        form = BlogpostForm()
        
    return(render(request, "blog/post.html", {
    "form" : form,    
    }))
    
def postDetail(request, id):
    post = Blogpost.objects.get(pk=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
            title = form.cleaned_data['title'],
            author = form.cleaned_data['author'],
            content = form.cleaned_data['content'],
            parent = post)
            comment.save()
            form = CommentForm()
        
    else:
        form = CommentForm()
        
    comments = Comment.objects.filter(parent__pk=id)
    
    return(render(request, "blog/post_details.html", {
    "form" : form, 
    "post": post,    
    "comments": comments,
    }))