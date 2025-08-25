from django.shortcuts import render
from django import forms


# Create your views here

from django.http import HttpResponse

def home(request):
    name = "Ali"
    context = {
        'name': 'ali'

    }
    return render ( request , "index.html", context )
# Simple Django form for name input
class SignUpForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)

def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Do something with the name (e.g., print or save it)
            return render(request, 'index.html', {
                'form': SignUpForm(),  # reset form
                'message': f'Thank you, {name}!'
            })
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form': form})
