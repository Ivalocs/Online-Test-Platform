from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserCreationForm, RegisterAsForm
from applicant.models import applicant_profile_model
from recruiter.models import recruiter_profile_model
from django.contrib.auth.models import User

# Create your views here.
def register_user(request):
    formA = CustomUserCreationForm()
    formB = RegisterAsForm()

    if request.method == 'POST':
        formA = CustomUserCreationForm(request.POST) #This is validating the process
        formB = RegisterAsForm(request.POST)
        registered_by = ''
        if formB.is_valid():
            registered_by = formB.cleaned_data['who']
        else:
            registered_by = 'Applicant'
        if formA.is_valid():
            new_user = formA.save(commit = False)
            new_user.username = new_user.username.lower()
            new_user.save()
            if registered_by  == 'Applicant':
                profile = applicant_profile_model.objects.create(
                    user = new_user,
                    username = new_user.username,
                    name = new_user.first_name
                )
            else:
                profile = recruiter_profile_model.objects.create(
                    user = new_user,
                    username = new_user.username,
                    name = new_user.first_name
                )
        context = {'page_id':1}
        return redirect("login")
    else:
        return redirect("login")
    context = {'formA':formA, 'formB':formB, 'page_id':2}
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        id = request.user.username
        try:
            applicant_user = applicant_profile_model.objects.get(username = id)
        except:
            applicant_user = None
        try:
            recruiter_user = recruiter_profile_model.objects.get(username = id)
        except:
            recruiter_user = None
        if applicant_user is not None:
            return redirect('applicant-profile', pk = applicant_user.username)
        else:
            return redirect('recruiter-profile', pk = recruiter_user.username)

    request.user.username
    if request.method == 'POST':
        id = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = id)
        except:
            user = None
            print('Username does not exist')
        
        user = authenticate(request, username = id, password = password)

        if user is not None:
            login(request, user)
            try:
                applicant_user = applicant_profile_model.objects.get(username = id)
            except:
                applicant_user = None
            try:
                recruiter_user = recruiter_profile_model.objects.get(username = id)
            except:
                recruiter_user = None
            
            if applicant_user is not None:
                return redirect('applicant-profile', pk = applicant_user.username)
            else:
                return redirect('recruiter-profile', pk = recruiter_user.username)
        else:
            print("ERROR")
    context = {'page_id':1}
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect("login")
