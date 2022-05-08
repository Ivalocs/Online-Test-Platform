from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import recruiter_profile_model

def recruiter_profile(request, pk):
    if request.user.is_authenticated:
        try:
            details = recruiter_profile_model.objects.get(username = pk)
        except:
            details = None
        if details is not None:
            context = {'details':details, 'page_id':4}
            return render(request, 'recruiter/recruiter-profile.html', context)
        else:
            print('Error')
            return redirect('login')
    else:
        return redirect('login')