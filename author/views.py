from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm,User,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

# def add_author(request):
#     if request.method=='POST':
#         author_form = forms.AuthorForms(request.POST)
#         if author_form.is_valid():
#             author_form.save()x
#             return redirect("add_auhtor")
        
#     else:
#         author_form = forms.AuthorForms()   
#     return render(request,"author/add_author.html",{'form':author_form})


def SignUp(request):
    if request.method=='POST':
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request,'Account Created Successfuly')
            return redirect("Login")
        
    else:
        signup_form = forms.SignupForm()   
    return render(request,"author/signup.html",{'form':signup_form, 'type':'SignUp'})

def userlogin(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            userpass=form.cleaned_data['password']
            user=authenticate(username=name,password=userpass)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                return redirect('signup')
            
    else:
        form=AuthenticationForm()
    return render(request,"author/signup.html",{'form':form, 'type':'Login'})



#----------user login using class based view------------

class Userloginview(LoginView):
    template_name='author/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Information Incorret')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['type']='Login'
        return context
    
    


@login_required       
def profile(request):     
    data=Post.objects.filter(author = request.user) 
    return render(request,"author/profile.html",{'data':data})



@login_required       
def updateprofile(request):
    if request.method=='POST':
            form=forms.UserchangeForm(request.POST,instance= request.user)
            if form.is_valid():
                messages.success(request,'Successfuly Updated')
                form.save()
                
    else:
        form=forms.UserchangeForm(instance= request.user)
    return render(request,"author/updateprofile.html",{'form':form})

@login_required
def userlogout(request):
    logout(request)
    return redirect('homepage')

#----------user logout using class based view------------

class Userlogoutview(LogoutView):
    def get_success_url(self):
        return self.get_redirect_url('homepage') 



    
@login_required
def passchange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated Successfully')
                update_session_auth_hash(request,form.user)
                return redirect('profile')
            
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,"author/passchange.html",{'form':form})
    else:
        return redirect('Login')

