from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    
    content={
        'username':request.user.get_username()
    }
    return render(request, 'dashboardPage/dashboard.html', content)
