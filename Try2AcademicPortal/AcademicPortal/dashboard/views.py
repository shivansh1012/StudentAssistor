import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import *

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    personal = Personal.objects.get(user=request.user.id)
    avatar = personal.avatar
    content={
        'username':request.user.get_username(),
        'avatar' : avatar,
    }
    return render(request, 'dashboardPage/dashboard.html', content)

@login_required(login_url='login')
def profile_view(request):
    username =Student.objects.get(user_id=request.user.id)
    personal = Personal.objects.get(user=request.user.id)
    context={
        'student':username,
        'name':username.name,
        'usn': username.usn,
        'sex': username.sex,
        'email': username.email,
        'branch':username.branch,
        'semester':username.sem,
        'course1':username.course1,
        'course2':username.course2,
        'course3':username.course3,
        'course4':username.course4,
        'course5':username.course5,
        'course6':username.course6,
        'avatar':personal.avatar,
        'bio':personal.bio,
        'website':personal.website,
        'linked':personal.linked,
        'github':personal.github,


    }
    return render(request,'dashboardPage/profile.html',context)

@login_required(login_url='login')
def update_profile_view(request):

    if request.method == 'POST':
        username = Student.objects.get(user_id=request.user.id)
        print(username)
        name = request.POST.get('name')
        email = request.POST.get('email')
        usn = request.POST.get('usn')
        sex = request.POST.get('sex')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        avatar = request.POST.get('avatar')
        website = request.POST.get('website')
        linked = request.POST.get('linked')
        github = request.POST.get('github')
        bio = request.POST.get('bio')
        courseid = {}
        coursename = {}
        for i in range(1,8):
            courseid['course'+str(i)] = request.POST.get('course'+str(i))
        print(courseid)
        json_data = open('static/dist/js/branch_sem_course.json')   
        data = json.load(json_data) # deserialises it
        json_data.close()
        #data2 = json.dumps(data1)  json formatted string
        for info in data:
            if info['id']==branch:
                branch = info['name']
            if info['id']==semester:
                semester = info['name']
            for i in range(1,8):
                if courseid['course'+str(i)]==info['id']:
                    coursename['course'+str(i)]= info['name']

        print(branch,semester)
        print(coursename)
        print(avatar)
        username.name=name
        username.email=email
        username.usn=usn
        username.sex=sex
        username.branch=branch
        username.sem=semester
        username.course1 = coursename['course1']
        username.course2 = coursename['course2']
        username.course3 = coursename['course3']
        username.course4 = coursename['course4']
        username.course5 = coursename['course5']
        username.course6 = coursename['course6']
        if avatar == 'Female1':
            src= "dist/img/avatar2.png"
        elif avatar == 'Female2':
            src= "dist/img/avatar3.png"
        elif avatar == 'Male1':
            src= "dist/img/avatar.png"
        elif avatar == 'Male2':
            src= "dist/img/avatar4.png"
        elif avatar == 'Male3':
            src= "dist/img/avatar5.png"
        personal = Personal.objects.get(user=request.user.id)
        personal.avatar = src
        personal.website = website
        personal.github = github
        personal.linked = linked
        personal.bio = bio
        personal.save()
        username.save()
        return redirect("dashboard:profile")
    context = {}
    return render(request,'dashboardPage/studentform.html',context)


def aboutus(request):
    personal = Personal.objects.get(user=request.user.id)
    avatar = personal.avatar
    content={
        'username':request.user.get_username(),
        'avatar' : avatar,
    }
    return render(request, 'dashboardPage/aboutus.html', content)