from django.shortcuts import render
from django import forms

# Updated form with name, email, and password
class SignUpForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Password should be hashed before saving in real apps
            password = form.cleaned_data['password']
            
            # For now, we just display a message
            return render(request, 'index.html', {
                'form': SignUpForm(),
                'message': f'Signed up as {name} ({email})!'
            })
        
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
