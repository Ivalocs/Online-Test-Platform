from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ExamCreationForm 
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import exam_details, exam_given
from recruiter.models import recruiter_profile_model


@login_required(login_url = "login")
def register_exam(request):
    exam_form = ExamCreationForm()
    if request.method == "POST":
        exam_form = ExamCreationForm(request.POST)
        if(exam_form.is_valid):
            print("valid form submitted!")
            exam_form.save(commit = False)
            try:
                recruiter_user = recruiter_profile_model.objects.get(username = request.user)
            except:
                recruiter_user = None

            if recruiter_user is not None:
                new_exam = exam_details.objects.create(
                    created_by = recruiter_user,
                    name = exam_form.cleaned_data['name'],
                    questions = exam_form.cleaned_data['questions'])
                aux = exam_given.objects.create(
                    name = recruiter_user,
                    exam = exam_form.cleaned_data['name']
                )
        return redirect("recruiter-profile", request.user)
    context = {"exam_form" : exam_form, "page_id" : 5, "username":request.user}
    return render(request, "exam/exam_form.html", context)

def take_test(request, pk):
    exam = exam_details.objects.get(id = pk)
    questions = exam.questions.split("#")
    problems = []
    for question in questions:
        q = question.split(",")[0]
        option = question.split(",")[1:-1]
        problems.append({"question" : q, "options" : {i:o for i, o in enumerate(option)}})
    context = {"questions":problems, "id" : exam.id, "test_name" : exam.name, "by_name" : exam.created_by.name}
    print(problems)
    return render(request, "exam/take_test.html", context)

def list_tests(request):
    tests = exam_details.objects.all()
    context = {"tests" : tests, "page_id" : 5, "username":request.user}
    return render(request, "exam/list_exams.html", context)


def report(request, pk):
    exam = exam_details.objects.get(id = pk)
    questions = exam.questions.split("#")
    display = [] 

    correct = 0
    incorrect = 0
    
    for question in questions:
        q = question.split(",")[0]
        if request.POST["radio_"+q] == question.split(",")[-1]:
            correct += 1
            display.append(q + " : correct")
        else:
            incorrect += 1
            display.append(q + " : incorrect")
    aux = exam_given.objects.create(
        name = request.user,
        exam = exam.name,
        correct = correct,
        incorrect = incorrect
    )
    context = {'display':display, 'correct':correct, 'incorrect':incorrect, 'page_id':6, 'username':request.user}
    return render(request, "exam/result.html", context)


        
