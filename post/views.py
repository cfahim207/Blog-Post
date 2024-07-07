from django.shortcuts import render,redirect
from .import forms
from django.urls import reverse_lazy

from .models import Post
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
@login_required 
def add_post(request):
    if request.method=='POST':
        post_form = forms.PostForms(request.POST)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect("add_post")
        
    else:
        post_form = forms.PostForms()   
    return render(request,"post/add_post.html",{'form':post_form})

#Add post using class based view
@method_decorator(login_required,name='dispatch')
class AddpostCreatView(CreateView):
    model =Post
    form_class = forms.PostForms
    template_name = 'post/add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        


@login_required 
def edit_post(request,id):
    post=Post.objects.get(pk=id)
    post_form = forms.PostForms(instance=post)
    if request.method=='POST':
        post_form = forms.PostForms(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect("profile")
    return render(request,"post/add_post.html",{'form':post_form})

#Edit post using class based view 
@method_decorator(login_required,name='dispatch')
class EditPostview(UpdateView):
    model=Post
    form_class=forms.PostForms
    template_name='post/add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')



@login_required 
def delete_post(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect("profile")

#Delete post using class based view 
@method_decorator(login_required,name='dispatch')
class DeletePostview(DeleteView):
    model=Post
    template_name='post/delete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')
    
    

#details post using class based view

class DetailspostView(DetailView):
    model=Post
    template_name='post/details.html'
    pk_url_kwarg='id'
    
    def post(self,request,*args, **kwargs):
        comment_form=forms.CommentForms(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save() 
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.CommentForms()  
            
        context['comments']=comments
        context['comment_form']=comment_form
        return context
    
    
    
    
    
