from django.shortcuts import render, redirect
from django import forms
import random
import string
from django.contrib.auth.models import User


# Sign-up form
class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
def login_view(request):
    email = request.session.get('email')  # Retrieve from session
    return render(request, 'login.html', {'email': email})

# Home view (sign-up page)
def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Dummy authentication check
            if email == 'admin@gmail.com' and password == '1234':
             request.session['email'] = email
             return redirect('login')

            else:
             return render(request, 'signup.html', {
                    'form': form,
                    'message': 'Invalid email or password.'
                })
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form,})

def generate_dummy_users(n):
    users = []
    for i in range(n):
        username = f"user{i}"
        email = f"user{i}@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        users.append({
            'username': username,
            'email': email,
            'password': password
        })
    return users

def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})