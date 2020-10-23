from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import SignUpForm

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('dashboard:home')
	else:
		form = SignUpForm()
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
		content = {'form':form}
		return render(request, 'registerPage/signup_page.html', content)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        content = {}
		
        return render(request, 'registerPage/login_page.html', content)

def logoutUser(request):
	logout(request)
	return redirect('login')