from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms




# Create your views here.
def home(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'form.html', {'form':form})

""" def Contactme(request):
  form = forms.FormName()

  if request.method == 'POST':
    form = forms.FormName()
    if form.is_valid():

      form.save()
      messages.success(request,'Your message has been sent sucesssfully!')
      return redirect('home') """