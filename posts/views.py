from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
	post = Post.objects.all()
	return render(request,'post/post_list.html',{'post':post})

# def post_list(request,slug):
# 	post_detail = Post.objects.get(slug=post_slug)
# 	return render(request,'post/post_detail.html',{'post_detail':post_detail})