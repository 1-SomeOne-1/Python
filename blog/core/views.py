from django.shortcuts import render, redirect
from django import forms

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
            if email == 'test@example.com' and password == 'password123':
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

