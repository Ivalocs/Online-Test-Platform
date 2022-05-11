from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from exam.models import exam_given

from .models import applicant_profile_model

def applicant_profile(request, pk):
    if request.user.is_authenticated:
        try:
            details = applicant_profile_model.objects.get(username = pk)
        except:
            details = None
        if details is not None:
            try:
                exam = exam_given.objects.filter(name = details.username)
            except exam_given.DoesNotExist:
                exam = None
            context = {'details':details, 'exam':exam, 'page_id':3}
            return render(request, 'applicant/applicant-profile.html', context)
        else:
            page = 1
            print('Error')
            return redirect('login')
    else:
        return redirect('login')
