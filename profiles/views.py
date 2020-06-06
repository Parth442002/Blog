from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.urls import reverse
# Create your views here.

class HomeView(TemplateView):
    template_name ='_base.html'

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            if not user.avatar:
                if user.gender=='Male':
                    user.avatar='avatars/male.svg'
                elif user.gender=='Female':
                    user.avatar=='avatars/female.svg'
                else:
                    user.avatar='avatars/default.svg'
            user.save()
            return redirect('home')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})
        


