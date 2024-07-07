from django.shortcuts import render
from post.models import Post
from categories.models import Category

def home(request,category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        categories=Category.objects.get(slug= category_slug)
        data=Post.objects.filter(category=categories)
    category=Category.objects.all()
    return render(request,'home.html',{'data':data,'category':category})