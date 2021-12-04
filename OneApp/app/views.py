"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.forms import BootstrapAuthenticationForm, RegisterForm, ChatForm, QuestionForm, AnswerForm
from app.models import Question, Chat
from django.views.generic import ListView



class chat(ListView):
    model = Chat
 
    def get_context_data(self, **kwargs):
        context = super(chat, self).get_context_data(**kwargs)
        return context

class question(ListView):
    model = Question
 
    def get_context_data(self, **kwargs):
        context = super(question, self).get_context_data(**kwargs)
        return context

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Us',
            'message':'Contact us using the email below and we will be sure to contact you within a reasonable time period.',
            'year':datetime.now().year,
        }
    )




def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def classes(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        qform = QuestionForm(request.POST or None)
        cform = ChatForm(request.POST or None)
        
        aform = AnswerForm(request.POST or None)

        if 'chat' in request.POST:
            
            if cform.is_valid():

                
                cform.save()
                response = redirect('/classes/?id=1')
            
                return response
        else:
            cform = ChatForm()

        if 'question' in request.POST:
      
            if qform.is_valid():

                qform.save()
                response = redirect('/classes/?id=2')
                return response
        else:
            qform = QuestionForm()

        if 'answer' in request.POST:
        
            if aform.is_valid():

                q=Question.objects.get(id=aform.cleaned_data['id'])
                string = aform.cleaned_data['answer']
                string = string.replace(",", "‚")
                q.answer.insert(0, string + " - Answered by: " + aform.cleaned_data['name'])
                q.save()

                response = redirect('/classes/?id=2')
            
                return response
        else:
            aform = AnswerForm()
    else:
        qform = QuestionForm(request.POST or None)
        cform = ChatForm(request.POST or None)
        aform = AnswerForm(request.POST or None)

    questions = Question.objects.all()

    chat = Chat.objects.all()

    
    return render(
            request,
            'app/classes.html',
            {
                'chats_list': chat,
                'questions_list': questions,
                'cform': cform,
                'qform': qform,
                'aform': aform,
            
                'title':'classes',
                'message':'Your application description page.',
                'year':datetime.now().year,
            }
        )

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if response.POST['email'].endswith('@mylaurier.ca'):
            if form.is_valid():
                form.save()
                
                return redirect("/login")

            else:
                return render(response, "app/register.html", {"form":form,'error' : 'Invalid User Name or Password: Place cursor over field for requirements.', 'title': 'Register',})

        else:

             return render(response, "app/register.html", {"form":form,'error' : 'Invalid Email: Please use your mylaurier.ca email.', 'title': 'Register',})
              

    else:
        form = RegisterForm()
   
    return render(response, "app/register.html", {"form":form, 'title': 'Register',})







