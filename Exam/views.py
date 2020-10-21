from django.shortcuts import render, redirect
from .models import Question, Category
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'Exam/home.html')


@login_required
def dashboard(request):
    choices = Category.objects.all()
    print(choices)
    return render(request, 'Exam/dashboard.html', {'choices':choices})


def register(request):
    msg = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            msg = "Please fill up the information correctly!!"
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form, 'msg':msg})


@login_required
def questions(request, choice):
    print(choice)
    ques = Question.objects.filter(catagory=choice)
    return render(request, 'Exam/questions.html', {'ques': ques})


@login_required
def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Question.objects.get(id=q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score / total) * 100
    return render(request, 'Exam/result.html', {'score': score,  'eff': eff, 'total': total})
