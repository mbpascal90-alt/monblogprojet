from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Creaccueil_viewate your views here.
def accueil_view(request):
      return render(request, 'accueil.html')

def connexion_view(request):
       if request.method =='POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                 user = form.get_user()
                 login(request, user)
                 return redirect('blogapp:accueil')
       else:
            form = AuthenticationForm()
      
       return render(request, 'connexion.html', {'form': form})

def inscription_view(request):
    if  request.method =='POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('blogapp:accueil')
    else:
                form = UserCreationForm()
      
    return render(request, 'inscription.html', {'form': form})

def deconnexion_view(request):
      logout(request)
      return redirect('blogapp:accueil')