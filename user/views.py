from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate,logout

# Create your views here.

# def register_view(request):
#   if request.user.is_authenticated:
#     return redirect('home_page')
  
#   if request.method == 'POST':
#     form = CreateUser(request.POST,request.FILES)
#     if form.is_valid():
#       form.save()
#       mail = form.cleaned_data.get('mail')
#       password = form.cleaned_data.get('password1')
#       user = authenticate(request, mail=mail,password=password)
#       print(mail,password)
#       login(request,user)
#       return redirect('home_page')
#     else:
#       form = CreateUser()
#       return render(request,'user/register.html',{
#         'form':form
#       })
#   form = CreateUser()
#   return render(request, 'user/register.html',{
#     'form':form
#   })



def register_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        form = CreateUser(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            mail = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=mail, password=password)
            login(request, new_user)  # Yeni kullanıcıyı oturum açmış olarak işaretle
            return redirect('home_page')
    else:
        form = CreateUser()

    return render(request, 'user/register.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
      form = LoginUser(request.POST)
      if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        username = User.objects.get(email = email).username
        print(email,username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home_page')
        else:
          return render(request,'user/login.html',{
            'form':form
          })
      else:
          return render(request,'user/login.html',{
            'form':form
          })
    else:
      form = LoginUser()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
  logout(request)
  return redirect('home_page')